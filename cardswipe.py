from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCardSwipe

KV = '''
<SwipeToDeleteItem>:
	size_hint_y:.5
	height:dp(100)
	MDCardSwipeLayerBox:
		MDFlatButton:
			size_hint:None,1
			text:"Remove"
			text_color:1,1,1,1
			on_release:app.removelist(root)
		
	MDCardSwipeFrontBox:
		TwoLineAvatarListItem:
			text:root.text
			secondary_text:"kivy"
			ImageLeftWidget:
				source:"data/logo/kivy-icon-256.png"
MDScreen:
	MDBoxLayout:
		orientation:"vertical"
		spacing:dp(10)
		MDToolbar:
			title:"youtube Histroy"
		ScrollView:
			scroll_timeout : 100
			MDList:
				id:box
				padding:0
			
			
			
			

'''


class SwipeToDeleteItem(MDCardSwipe):
    text=StringProperty()

class TestCard(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        return self.screen
    def removelist(self,instance):
    	self.root.ids.box.remove_widget(instance)
    def on_start(self):
    	for i in range(20):
    		self.root.ids.box.add_widget(SwipeToDeleteItem(text=f"kivymd {i}"))
    	
TestCard().run()