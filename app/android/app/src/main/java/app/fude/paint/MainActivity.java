package app.fude.paint;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(NowPlayingPlugin.class);
        super.onCreate(savedInstanceState);
        openShared(getIntent());
    }

    @Override
    protected void onNewIntent(Intent intent) {
        super.onNewIntent(intent);
        openShared(intent);
    }

    // a song shared from a music app's Share menu: Fude reads it from ?text=… and ?title=…
    private void openShared(Intent intent) {
        if (intent == null || !Intent.ACTION_SEND.equals(intent.getAction()) || bridge == null) return;
        String text = intent.getStringExtra(Intent.EXTRA_TEXT);
        if (text == null) return;
        String subject = intent.getStringExtra(Intent.EXTRA_SUBJECT);
        String url = bridge.getLocalUrl() + "/?text=" + Uri.encode(text) + (subject != null ? "&title=" + Uri.encode(subject) : "");
        bridge.getWebView().post(() -> bridge.getWebView().loadUrl(url));
        intent.setAction(Intent.ACTION_MAIN);
    }
}
