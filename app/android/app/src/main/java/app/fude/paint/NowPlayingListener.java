package app.fude.paint;

import android.service.notification.NotificationListenerService;

// Android only shares what other apps are playing with an app the user has given notification access.
// Fude reads no notifications: this service only has to exist so the access can be granted.
public class NowPlayingListener extends NotificationListenerService {}
