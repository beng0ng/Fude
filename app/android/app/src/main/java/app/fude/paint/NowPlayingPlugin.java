package app.fude.paint;

import android.content.ComponentName;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.media.MediaMetadata;
import android.media.session.MediaController;
import android.media.session.MediaSessionManager;
import android.media.session.PlaybackState;
import android.os.Build;
import android.os.Handler;
import android.os.Looper;
import android.os.SystemClock;
import android.provider.Settings;
import android.util.Base64;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import java.io.ByteArrayOutputStream;
import java.util.List;

// What is playing in other apps (Spotify, YouTube Music, anything with media controls): the song, its cover,
// where it is and whether it plays, so Fude can follow the music when it goes to headphones and the microphone hears nothing.
// Everything stays on the phone.
@CapacitorPlugin(name = "NowPlaying")
public class NowPlayingPlugin extends Plugin {
    private final Handler main = new Handler(Looper.getMainLooper());
    private MediaSessionManager sessions;
    private MediaController controller;
    private boolean watching = false;
    private String artKey = "";
    private String art = "";

    private ComponentName listener() {
        return new ComponentName(getContext(), NowPlayingListener.class);
    }

    private boolean allowed() {
        String on = Settings.Secure.getString(getContext().getContentResolver(), "enabled_notification_listeners");
        if (on == null) return false;
        String me = listener().flattenToString(), shortMe = listener().flattenToShortString();
        for (String s : on.split(":")) if (s.equals(me) || s.equals(shortMe)) return true;
        return false;
    }

    @PluginMethod
    public void status(PluginCall call) {
        JSObject r = new JSObject();
        r.put("allowed", allowed());
        call.resolve(r);
    }

    // the system page where Fude's access is turned on; Android 11 and later can open Fude's own switch directly
    @PluginMethod
    public void openSettings(PluginCall call) {
        Intent i = null;
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            i = new Intent(Settings.ACTION_NOTIFICATION_LISTENER_DETAIL_SETTINGS);
            i.putExtra(Settings.EXTRA_NOTIFICATION_LISTENER_COMPONENT_NAME, listener().flattenToString());
            if (i.resolveActivity(getContext().getPackageManager()) == null) i = null;
        }
        if (i == null) i = new Intent(Settings.ACTION_NOTIFICATION_LISTENER_SETTINGS);
        i.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
        try {
            getContext().startActivity(i);
            call.resolve();
        } catch (Exception e) {
            call.reject("Could not open settings", e);
        }
    }

    @PluginMethod
    public void start(PluginCall call) {
        if (!allowed()) {
            call.reject("Notification access is off", "DENIED");
            return;
        }
        main.post(() -> {
            try {
                if (sessions == null) sessions = (MediaSessionManager) getContext().getSystemService(android.content.Context.MEDIA_SESSION_SERVICE);
                if (!watching) {
                    sessions.addOnActiveSessionsChangedListener(changed, listener(), main);
                    watching = true;
                }
                choose(sessions.getActiveSessions(listener()));
                call.resolve(info());
            } catch (SecurityException e) {
                call.reject("Notification access is off", "DENIED", e);
            }
        });
    }

    @PluginMethod
    public void stop(PluginCall call) {
        main.post(() -> {
            unwatch();
            call.resolve();
        });
    }

    @PluginMethod
    public void current(PluginCall call) {
        main.post(() -> call.resolve(info()));
    }

    // play, pause and skip, sent to the app that is playing
    @PluginMethod
    public void control(PluginCall call) {
        String action = call.getString("action", "");
        main.post(() -> {
            if (controller == null) {
                call.reject("Nothing is playing", "NONE");
                return;
            }
            MediaController.TransportControls t = controller.getTransportControls();
            switch (action) {
                case "play": t.play(); break;
                case "pause": t.pause(); break;
                case "next": t.skipToNext(); break;
                case "previous": t.skipToPrevious(); break;
                default: call.reject("Unknown action"); return;
            }
            call.resolve();
        });
    }

    @Override
    protected void handleOnDestroy() {
        unwatch();
    }

    private void unwatch() {
        if (watching && sessions != null) sessions.removeOnActiveSessionsChangedListener(changed);
        watching = false;
        if (controller != null) controller.unregisterCallback(callback);
        controller = null;
    }

    private final MediaSessionManager.OnActiveSessionsChangedListener changed = this::choose;

    private final MediaController.Callback callback = new MediaController.Callback() {
        @Override
        public void onMetadataChanged(MediaMetadata metadata) {
            send();
        }

        @Override
        public void onPlaybackStateChanged(PlaybackState state) {
            // another app may have started playing while this one paused
            if (sessions != null && watching && (state == null || !isPlaying(state))) {
                try {
                    choose(sessions.getActiveSessions(listener()));
                    return;
                } catch (SecurityException e) {
                    // access was turned off; keep the last app
                }
            }
            send();
        }

        @Override
        public void onSessionDestroyed() {
            if (controller != null) controller.unregisterCallback(this);
            controller = null;
            try {
                if (sessions != null && watching) choose(sessions.getActiveSessions(listener()));
            } catch (SecurityException e) {
                send();
            }
        }
    };

    private static boolean isPlaying(PlaybackState s) {
        int st = s.getState();
        return st == PlaybackState.STATE_PLAYING || st == PlaybackState.STATE_BUFFERING;
    }

    // the app that is playing, or else the one that played last
    private void choose(List<MediaController> list) {
        MediaController pick = null;
        if (list != null) {
            for (MediaController c : list) {
                PlaybackState s = c.getPlaybackState();
                if (s != null && isPlaying(s)) {
                    pick = c;
                    break;
                }
            }
            if (pick == null && controller != null) {
                for (MediaController c : list) if (c.getSessionToken().equals(controller.getSessionToken())) pick = controller;
            }
            if (pick == null && !list.isEmpty()) pick = list.get(0);
        }
        if (pick == null || controller == null || !pick.getSessionToken().equals(controller.getSessionToken())) {
            if (controller != null) controller.unregisterCallback(callback);
            controller = pick;
            if (controller != null) controller.registerCallback(callback, main);
        }
        send();
    }

    private void send() {
        notifyListeners("change", info());
    }

    private JSObject info() {
        JSObject r = new JSObject();
        MediaController c = controller;
        MediaMetadata md = c == null ? null : c.getMetadata();
        if (c == null || md == null) {
            r.put("playing", false);
            return r;
        }
        String pkg = c.getPackageName(), title = text(md, MediaMetadata.METADATA_KEY_TITLE, MediaMetadata.METADATA_KEY_DISPLAY_TITLE);
        String artist = text(md, MediaMetadata.METADATA_KEY_ARTIST, MediaMetadata.METADATA_KEY_ALBUM_ARTIST, MediaMetadata.METADATA_KEY_DISPLAY_SUBTITLE);
        long dur = md.getLong(MediaMetadata.METADATA_KEY_DURATION);
        PlaybackState s = c.getPlaybackState();
        boolean playing = s != null && isPlaying(s);
        long pos = 0;
        if (s != null) {
            pos = s.getPosition();
            if (playing && s.getLastPositionUpdateTime() > 0) pos += (long) ((SystemClock.elapsedRealtime() - s.getLastPositionUpdateTime()) * s.getPlaybackSpeed());
            if (dur > 0) pos = Math.max(0, Math.min(pos, dur));
        }
        r.put("id", pkg + "|" + title + "|" + artist + "|" + dur);
        r.put("title", title);
        r.put("artist", artist);
        r.put("album", text(md, MediaMetadata.METADATA_KEY_ALBUM));
        r.put("duration", Math.max(0, dur));
        r.put("position", pos);
        r.put("playing", playing);
        r.put("package", pkg);
        r.put("app", appName(pkg));
        r.put("art", cover(md, pkg + "|" + title + "|" + artist));
        return r;
    }

    private static String text(MediaMetadata md, String... keys) {
        for (String k : keys) {
            CharSequence v = md.getText(k);
            if (v != null && v.length() > 0) return v.toString();
        }
        return "";
    }

    private String appName(String pkg) {
        try {
            PackageManager pm = getContext().getPackageManager();
            return pm.getApplicationLabel(pm.getApplicationInfo(pkg, 0)).toString();
        } catch (Exception e) {
            return "";
        }
    }

    // the cover, made small and sent as a picture the page can read; worked out once per song
    private String cover(MediaMetadata md, String key) {
        if (key.equals(artKey)) return art;
        Bitmap b = md.getBitmap(MediaMetadata.METADATA_KEY_ALBUM_ART);
        if (b == null) b = md.getBitmap(MediaMetadata.METADATA_KEY_ART);
        if (b == null) b = md.getBitmap(MediaMetadata.METADATA_KEY_DISPLAY_ICON);
        String out = "";
        if (b != null) {
            try {
                int w = b.getWidth(), h = b.getHeight();
                float k = Math.min(1f, 300f / Math.max(w, h));
                Bitmap small = k < 1f ? Bitmap.createScaledBitmap(b, Math.max(1, Math.round(w * k)), Math.max(1, Math.round(h * k)), true) : b;
                ByteArrayOutputStream o = new ByteArrayOutputStream();
                small.compress(Bitmap.CompressFormat.JPEG, 85, o);
                out = "data:image/jpeg;base64," + Base64.encodeToString(o.toByteArray(), Base64.NO_WRAP);
            } catch (Exception e) {
                out = "";
            }
        }
        // a cover that arrives a moment after the song is picked up on the next change
        if (!out.isEmpty()) artKey = key;
        art = out;
        return out;
    }
}
