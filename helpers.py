from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from functools import partial

KV = '''
BoxLayout:
    orientation: 'vertical'

    ScreenManager:
        id: screen_manager

        Screen:
            name: 'login_screen'

            MDScreen:
                MDTextField:
                    id: username
                    hint_text: "Username"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.7}
                    size_hint_x: None
                    width: 300

                MDTextField:
                    id: password
                    hint_text: "Password"
                    password: True
                    pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                    size_hint_x: None
                    width: 300

                MDRaisedButton:
                    text: "Login"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.login()

        Screen:
            name: 'page1'

            MDScreen:
                MDRaisedButton:
                    text: "Nifty Fifty Companies"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_release: app.change_screen('page2')

        Screen:
            name: 'page2'

            BoxLayout:
                orientation: 'vertical'

                MDTextField:
                    id: search_input
                    hint_text: "Search for the companies here"
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.95}
                    size_hint_x: None
                    width: 300
                    on_text: app.update_suggestions()

                ScrollView:
                    MDList:
                        id: company_list

        Screen:
            name: 'page3'

            MDScreen:
                MDLabel:
                    id: selected_company_label
                    text: "Selected Company: "
                    halign: 'center'
                    theme_text_color: "Secondary"
                    font_style: 'H6'
                    size_hint_y: None
                    height: "48dp"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.8}

                MDIconButton:
                    icon: "calendar-month"
                    pos_hint: {'center_x': 0.63, 'center_y': 0.5}
                    on_release: app.show_date_picker()

                MDTextField:
                    id: selected_date
                    hint_text: "Prediction Date"
                    pos_hint: {'center_x': 0.45, 'center_y': 0.5}
                    size_hint_x: None
                    width: 300

                MDRaisedButton:
                    text: "Continue"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: app.change_screen('page4')

        # Add this block in your KV string
        Screen:
            name: 'page4'

            BoxLayout:
                orientation: 'vertical'

                MDTextField:
                    id: some_textfield
                    hint_text: "Some Text Field"
                    size_hint_y: None
                    height: "40dp"

                MDFillRoundFlatButton:
                    text: "Go Back to Page 3"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                    on_release: app.change_screen('page2')
'''

class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        self.populate_company_list()

    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        # Add your authentication logic here
        # For demonstration purposes, let's use a simple check
        if username == 'user' and password == 'password':
            self.change_screen('page1')
        else:
            print("Invalid credentials")

    def change_screen(self, screen_name):
        self.root.ids.screen_manager.current = screen_name

    def handle_company_selection(self, instance, company_name_str):
        print(f"Selected company: {company_name_str}")
        self.root.ids.selected_company_label.text = f"Selected Company: {company_name_str}"
        self.change_screen('page3')

    def populate_company_list(self):
        # Define list items individually
        item1 = OneLineListItem(text="Adani Ports & SEZ", on_release=lambda instance: self.handle_company_selection(instance, "Adani Ports & SEZ"))
        item2 = OneLineListItem(text="Asian Paints", on_release=lambda instance: self.handle_company_selection(instance, "Asian Paints"))
        item3 = OneLineListItem(text="Axis Bank", on_release=lambda instance: self.handle_company_selection(instance, "Axis Bank"))
        item4 = OneLineListItem(text="Bajaj Auto", on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Auto"))
        item5= OneLineListItem(text="Bajaj Finance", on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Finance"))
        item6 = OneLineListItem(text="Bajaj Finserv", on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Finserv"))
        item7 = OneLineListItem(text="Bharti Airtel", on_release=lambda instance: self.handle_company_selection(instance, "Bharti Airtel"))
        item8 = OneLineListItem(text="Bharti Infratel", on_release=lambda instance: self.handle_company_selection(instance, "Bharti Infratel"))
        item9 = OneLineListItem(text="Cipla", on_release=lambda instance: self.handle_company_selection(instance, "Cipla"))
        item10 = OneLineListItem(text="Coal India", on_release=lambda instance: self.handle_company_selection(instance, "Coal India"))
        item11= OneLineListItem(text="Dr.Reddy's Laboratories", on_release=lambda instance: self.handle_company_selection(instance, "Dr.Reddy's Laboratories"))
        item12 = OneLineListItem(text="Eicher Motors", on_release=lambda instance: self.handle_company_selection(instance, "Eicher Motors"))
        item13 = OneLineListItem(text="GAIL (India)", on_release=lambda instance: self.handle_company_selection(instance, "GAIL (India)"))
        item14= OneLineListItem(text="Grasim Industries", on_release=lambda instance: self.handle_company_selection(instance, "Grasim Industries"))
        item16= OneLineListItem(text="Hindustan Unilever", on_release=lambda instance: self.handle_company_selection(instance, "Hindustan Unilever"))
        item17 = OneLineListItem(text="ICICI Bank", on_release=lambda instance: self.handle_company_selection(instance, "ICICI Bank"))
        item18 = OneLineListItem(text="IndusInd Bank", on_release=lambda instance: self.handle_company_selection(instance, "IndusInd Bank"))
        item19= OneLineListItem(text="Infosys", on_release=lambda instance: self.handle_company_selection(instance, "Infosys"))
        item20= OneLineListItem(text="IOC (Indian Oil Corporation)", on_release=lambda instance: self.handle_company_selection(instance, "IOC (Indian Oil Corporation)"))
        item21 = OneLineListItem(text="ITC", on_release=lambda instance: self.handle_company_selection(instance, "ITC"))
        item22 = OneLineListItem(text="JSW Steel", on_release=lambda instance: self.handle_company_selection(instance, "JSW Steel"))
        item23 = OneLineListItem(text="Kotak Mahindra Bank", on_release=lambda instance: self.handle_company_selection(instance, "Kotak Mahindra Bank"))
        item24 = OneLineListItem(text="L&T (Larsen & Toubro)", on_release=lambda instance: self.handle_company_selection(instance, "L&T (Larsen & Toubro)"))
        item25 = OneLineListItem(text="M&M (Mahindra & Mahindra)", on_release=lambda instance: self.handle_company_selection(instance, "M&M (Mahindra & Mahindra)"))
        item26 = OneLineListItem(text="Maruti Suzuki", on_release=lambda instance: self.handle_company_selection(instance, "Maruti Suzuki"))
        item27= OneLineListItem(text="Nestle India", on_release=lambda instance: self.handle_company_selection(instance, "Nestle India"))
        item28 = OneLineListItem(text="NTPC", on_release=lambda instance: self.handle_company_selection(instance, "NTPC"))
        item29 = OneLineListItem(text="ONGC", on_release=lambda instance: self.handle_company_selection(instance, "ONGC"))
        item30 = OneLineListItem(text="Power Grid Corporation of India", on_release=lambda instance: self.handle_company_selection(instance, "Power Grid Corporation of India"))
        item31 = OneLineListItem(text="Reliance Industries", on_release=lambda instance: self.handle_company_selection(instance, "Reliance Industries"))
        item32 = OneLineListItem(text="Shree Cements", on_release=lambda instance: self.handle_company_selection(instance, "Shree Cements"))
        item33= OneLineListItem(text="Sun Pharmaceutical Industries", on_release=lambda instance: self.handle_company_selection(instance, "Sun Pharmaceutical Industries"))
        item34 = OneLineListItem(text="Tata Motors", on_release=lambda instance: self.handle_company_selection(instance, "Tata Motors"))
        item35 = OneLineListItem(text="Tata Steel", on_release=lambda instance: self.handle_company_selection(instance, "TATASTEEL.NS"))
        item36 = OneLineListItem(text="TCS (Tata Consultancy Services)", on_release=partial(self.handle_company_selection, "TCS (Tata Consultancy Services)"))
        item37= OneLineListItem(text="Tech Mahindra", on_release=lambda instance: self.handle_company_selection(instance, "Tech Mahindra"))
        item38= OneLineListItem(text="Titan Company", on_release=lambda instance: self.handle_company_selection(instance, "Titan Company"))
        item39= OneLineListItem(text="UltraTech Cement", on_release=lambda instance: self.handle_company_selection(instance, "UltraTech Cement"))
        item40= OneLineListItem(text="UPL", on_release=lambda instance: self.handle_company_selection(instance, "UPL"))
        item41= OneLineListItem(text="Wipro", on_release=lambda instance: self.handle_company_selection(instance, "Wipro"))
        item42= OneLineListItem(text="Zee Entertainment Enterprises", on_release=lambda instance: self.handle_company_selection(instance, "Zee Entertainment Enterprises"))

        # Add more items as needed

        # Add items to the list
        self.root.ids.company_list.add_widget(item1)
        self.root.ids.company_list.add_widget(item2)
        self.root.ids.company_list.add_widget(item3)
        self.root.ids.company_list.add_widget(item4)
        self.root.ids.company_list.add_widget(item5)
        self.root.ids.company_list.add_widget(item6)
        self.root.ids.company_list.add_widget(item7)
        self.root.ids.company_list.add_widget(item8)
        self.root.ids.company_list.add_widget(item9)
        self.root.ids.company_list.add_widget(item10)
        self.root.ids.company_list.add_widget(item11)
        self.root.ids.company_list.add_widget(item12)
        self.root.ids.company_list.add_widget(item13)
        self.root.ids.company_list.add_widget(item14)
        self.root.ids.company_list.add_widget(item16)
        self.root.ids.company_list.add_widget(item18)
        self.root.ids.company_list.add_widget(item19)
        self.root.ids.company_list.add_widget(item20)
        self.root.ids.company_list.add_widget(item21)
        self.root.ids.company_list.add_widget(item22)
        self.root.ids.company_list.add_widget(item23)
        self.root.ids.company_list.add_widget(item24)
        self.root.ids.company_list.add_widget(item25)
        self.root.ids.company_list.add_widget(item26)
        self.root.ids.company_list.add_widget(item27)
        self.root.ids.company_list.add_widget(item28)
        self.root.ids.company_list.add_widget(item29)
        self.root.ids.company_list.add_widget(item30)
        self.root.ids.company_list.add_widget(item31)
        self.root.ids.company_list.add_widget(item33)
        self.root.ids.company_list.add_widget(item34)
        self.root.ids.company_list.add_widget(item35)
        self.root.ids.company_list.add_widget(item36)
        self.root.ids.company_list.add_widget(item37)
        self.root.ids.company_list.add_widget(item38)
        self.root.ids.company_list.add_widget(item39)
        self.root.ids.company_list.add_widget(item40)
        self.root.ids.company_list.add_widget(item41)
        self.root.ids.company_list.add_widget(item42)
        # Add more items as needed

    def update_suggestions(self):
        search_text = self.root.ids.search_input.text.lower()
        self.root.ids.company_list.clear_widgets()

        # Define list items individually and add them based on the search text
        item1 = OneLineListItem(text="Adani Ports & SEZ", on_release=lambda instance: self.handle_company_selection(instance, "Adani Ports & SEZ"))
        item2 = OneLineListItem(text="Asian Paints", on_release=lambda instance: self.handle_company_selection(instance, "Asian Paints"))
        item3 = OneLineListItem(text="Axis Bank", on_release=lambda instance: self.handle_company_selection(instance, "Axis Bank"))
        item4 = OneLineListItem(text="Bajaj Auto", on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Auto"))
        item5 = OneLineListItem(text="Bajaj Finance",
                                on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Finance"))
        item6 = OneLineListItem(text="Bajaj Finserv",
                                on_release=lambda instance: self.handle_company_selection(instance, "Bajaj Finserv"))
        item7 = OneLineListItem(text="Bharti Airtel",
                                on_release=lambda instance: self.handle_company_selection(instance, "Bharti Airtel"))
        item8 = OneLineListItem(text="Bharti Infratel",
                                on_release=lambda instance: self.handle_company_selection(instance, "Bharti Infratel"))
        item9 = OneLineListItem(text="Cipla", on_release=lambda instance: self.handle_company_selection(instance, "Cipla"))
        item10 = OneLineListItem(text="Coal India", on_release=lambda instance: self.handle_company_selection(instance, "Coal India"))
        item11 = OneLineListItem(text="Dr.Reddy's Laboratories",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Dr.Reddy's Laboratories"))
        item12 = OneLineListItem(text="Eicher Motors",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Eicher Motors"))
        item13 = OneLineListItem(text="GAIL (India)", on_release=lambda instance: self.handle_company_selection(instance, "GAIL (India)"))
        item14 = OneLineListItem(text="Grasim Industries",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Grasim Industries"))
        item16 = OneLineListItem(text="Hindustan Unilever",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Hindustan Unilever"))
        item17 = OneLineListItem(text="ICICI Bank", on_release=lambda instance: self.handle_company_selection(instance, "ICICI Bank"))
        item18 = OneLineListItem(text="IndusInd Bank",
                                 on_release=lambda instance: self.handle_company_selection(instance, "IndusInd Bank"))
        item19 = OneLineListItem(text="Infosys", on_release=lambda instance: self.handle_company_selection(instance, "Infosys"))
        item20 = OneLineListItem(text="IOC (Indian Oil Corporation)",
                                 on_release=lambda instance: self.handle_company_selection(instance, "IOC (Indian Oil Corporation)"))
        item21 = OneLineListItem(text="ITC", on_release=lambda instance: self.handle_company_selection(instance, "ITC"))
        item22 = OneLineListItem(text="JSW Steel", on_release=lambda instance: self.handle_company_selection(instance, "JSW Steel"))
        item23 = OneLineListItem(text="Kotak Mahindra Bank",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Kotak Mahindra Bank"))
        item24 = OneLineListItem(text="L&T (Larsen & Toubro)",
                                 on_release=lambda instance: self.handle_company_selection(instance, "L&T (Larsen & Toubro)"))
        item25 = OneLineListItem(text="M&M (Mahindra & Mahindra)",
                                 on_release=lambda instance: self.handle_company_selection(instance, "M&M (Mahindra & Mahindra)"))
        item26 = OneLineListItem(text="Maruti Suzuki",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Maruti Suzuki"))
        item27 = OneLineListItem(text="Nestle India", on_release=lambda instance: self.handle_company_selection(instance, "Nestle India"))
        item28 = OneLineListItem(text="NTPC", on_release=lambda instance: self.handle_company_selection(instance, "NTPC"))
        item29 = OneLineListItem(text="ONGC", on_release=lambda instance: self.handle_company_selection(instance, "ONGC"))
        item30 = OneLineListItem(text="Power Grid Corporation of India",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Power Grid Corporation of India"))
        item31 = OneLineListItem(text="Reliance Industries",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Reliance Industries"))
        item32 = OneLineListItem(text="Shree Cements",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Shree Cements"))
        item33 = OneLineListItem(text="Sun Pharmaceutical Industries",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Sun Pharmaceutical Industries"))
        item34 = OneLineListItem(text="Tata Motors", on_release=lambda instance: self.handle_company_selection(instance, "Tata Motors"))
        item35 = OneLineListItem(text="Tata Steel", on_release=lambda instance: self.handle_company_selection(instance, "TATASTEEL.NS"))
        item36 = OneLineListItem(text="TCS (Tata Consultancy Services)",
                                 on_release=lambda instance: self.handle_company_selection(instance, "TCS (Tata Consultancy Services)"))
        item37 = OneLineListItem(text="Tech Mahindra",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Tech Mahindra"))
        item38 = OneLineListItem(text="Titan Company",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Titan Company"))
        item39 = OneLineListItem(text="UltraTech Cement",
                                 on_release=lambda instance: self.handle_company_selection(instance, "UltraTech Cement"))
        item40 = OneLineListItem(text="UPL", on_release=lambda instance: self.handle_company_selection(instance, "UPL"))
        item41 = OneLineListItem(text="Wipro", on_release=lambda instance: self.handle_company_selection(instance, "Wipro"))
        item42 = OneLineListItem(text="Zee Entertainment Enterprises",
                                 on_release=lambda instance: self.handle_company_selection(instance, "Zee Entertainment Enterprises"))

        # Add more items as needed

        # Add items to the list
        self.root.ids.company_list.add_widget(item1)
        self.root.ids.company_list.add_widget(item2)
        self.root.ids.company_list.add_widget(item3)
        self.root.ids.company_list.add_widget(item4)
        self.root.ids.company_list.add_widget(item5)
        self.root.ids.company_list.add_widget(item6)
        self.root.ids.company_list.add_widget(item7)
        self.root.ids.company_list.add_widget(item8)
        self.root.ids.company_list.add_widget(item9)
        self.root.ids.company_list.add_widget(item10)
        self.root.ids.company_list.add_widget(item11)
        self.root.ids.company_list.add_widget(item12)
        self.root.ids.company_list.add_widget(item13)
        self.root.ids.company_list.add_widget(item14)
        self.root.ids.company_list.add_widget(item16)
        self.root.ids.company_list.add_widget(item18)
        self.root.ids.company_list.add_widget(item19)
        self.root.ids.company_list.add_widget(item20)
        self.root.ids.company_list.add_widget(item21)
        self.root.ids.company_list.add_widget(item22)
        self.root.ids.company_list.add_widget(item23)
        self.root.ids.company_list.add_widget(item24)
        self.root.ids.company_list.add_widget(item25)
        self.root.ids.company_list.add_widget(item26)
        self.root.ids.company_list.add_widget(item27)
        self.root.ids.company_list.add_widget(item28)
        self.root.ids.company_list.add_widget(item29)
        self.root.ids.company_list.add_widget(item30)
        self.root.ids.company_list.add_widget(item31)
        self.root.ids.company_list.add_widget(item33)
        self.root.ids.company_list.add_widget(item34)
        self.root.ids.company_list.add_widget(item35)
        self.root.ids.company_list.add_widget(item36)
        self.root.ids.company_list.add_widget(item37)
        self.root.ids.company_list.add_widget(item38)
        self.root.ids.company_list.add_widget(item39)
        self.root.ids.company_list.add_widget(item40)
        self.root.ids.company_list.add_widget(item41)
        self.root.ids.company_list.add_widget(item42)

        # Add more items as needed

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        selected_date_text = f" {value.strftime('%d-%m-%Y')}"
        self.root.ids.selected_date.text = selected_date_text
        self.predictdate = value  # Store the selected date in the variable predictdate
        print(value)

if __name__ == '__main__':
    MyApp().run()
