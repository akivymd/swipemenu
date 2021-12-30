from kivy.lang.builder import Builder
from kivymd.uix.list import OneLineListItem
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd_extensions.akivymd import*
Builder.load_string(
  """
<SwipeMenu>
	AKSwipeMenu:
		id:menu
		on_open:but.icon="arrow-down"
		on_dismiss:but.icon="arrow-up"
		AKSwipeMenuMainContent:
			orientation:"vertical"
			ScrollView:
				MDBoxLayout:
					orientation:"vertical"
					size_hint:1,.35
					Image:
						id:a
						source:"kivy-icon-256.png"
		AKSwipeMenuTopContent:
			MDBoxLayout:
				size_hint_y:None
				height:dp(60)
				padding:dp(10)
				MDLabel:
					text:"Swipe up to see playlist"
					valign:"center"
					text_color:1,1,1,1
				MDIconButton:
					id:but
					icon:"arrow-up"
					pos_hint:{"center_y":.5}
					on_release:
						if menu.get_status()=="close": menu.open()
						else:menu.dismiss()
		AKSwipeMenuBottomContent:
			MDBoxLayout:
				orientation:"vertical"
				size_hint_y:None
				height:dp(180)
				OneLineAvatarListItem:
					text:"kivymd image"
					divider:None
					on_release:a.source="drawer_logo.png"
					ImageLeftWidget:
						source:"drawer_logo.png"
				OneLineAvatarListItem:
					text:"kivymd style image"
					divider:None
					on_release:a.source="logo-kivymd.png"
					ImageLeftWidget:
						source:"logo-kivymd.png"
				OneLineAvatarListItem:
					text:"kivy image"
					divider:None
					on_release:a.source="kivy-icon-256.png"
					ImageLeftWidget:
						source:"kivy-icon-256.png"
						
		
"""
)
class SwipeMenu(MDScreen):
	pass

class Test(MDApp):
    def build(self):
        self.piechart = SwipeMenu()
        return self.piechart

Test().run()
