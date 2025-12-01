from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget

# Java / Android imports via pyjnius
from jnius import autoclass
from android.runnable import run_on_ui_thread

# Android classes we need
PythonActivity = autoclass("org.kivy.android.PythonActivity")
WebView = autoclass("android.webkit.WebView")
WebViewClient = autoclass("android.webkit.WebViewClient")
LinearLayout = autoclass("android.widget.LinearLayout")
LayoutParams = autoclass("android.view.ViewGroup$LayoutParams")

# Change this to the site you want to display
TARGET_URL = "https://mishbahop.github.io/site-h-vro/"


class WebViewApp(App):
    def build(self):
        # Build a minimal Kivy root; real UI is the native WebView
        Clock.schedule_once(lambda dt: self._init_webview(), 0)
        return Widget()

    @run_on_ui_thread
    def _init_webview(self, *_):
        activity = PythonActivity.mActivity

        webview = WebView(activity)
        webview.getSettings().setJavaScriptEnabled(True)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl(TARGET_URL)

        layout = LinearLayout(activity)
        layout.setOrientation(LinearLayout.VERTICAL)
        layout.addView(
            webview,
            LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT),
        )

        activity.setContentView(layout)
        self.webview = webview

    def on_stop(self):
        if hasattr(self, "webview"):
            self.webview.destroy()


if __name__ == "__main__":
    WebViewApp().run()
