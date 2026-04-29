from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class EyeCareApp(App):
    def build(self):
        # 画面のレイアウト（縦に並べる）
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # 文字を表示するラベル
        self.label = Label(text="目を守る準備はいい？", font_size='20sp')
        
        # スタートボタン
        self.btn = Button(text="タイマーをスタート！", size_hint=(1, 0.3))
        self.btn.bind(on_press=self.start_timer)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn)
        return self.layout

    def start_timer(self, instance):
        self.label.text = "20分後に通知するよ！"
        self.btn.disabled = True
        # 1200秒（20分）後にメッセージを出す
        Clock.schedule_once(self.show_break_message, 1200)

    def show_break_message(self, dt):
        self.label.text = "休憩の時間！\n20秒間、遠くを見てね！"
        self.btn.disabled = False
        self.btn.text = "もう一度スタート"

if __name__ == '__main__':
    EyeCareApp().run()
