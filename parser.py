from object import Item
from lxml import html

class Parser:

    def parse_object(self, content):
        tree = html.fromstring(content) 
        answer = []
        length = len(tree.xpath('//*[@id="main_table_countries_today"]/tbody[1]/text()'))
        for idx in range(9,length):
            item =  Item(
                property_1=self.get_property_1(tree,idx),
                property_2=self.get_property_2(tree,idx),
                property_3=self.get_property_3(tree,idx),
                property_4=self.get_property_4(tree,idx),
                property_5=self.get_property_5(tree,idx)
            )
            if not item.property_1 == " ":
                answer.append(item)
        return answer
       

    def get_property_1(self, tree,idx):
        answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[2]/a/text()')
        if len(answer) == 0:
            answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[2]/text()')
        return " " if len(answer)==0 else answer[0].replace(",",".")  

    def get_property_2(self, tree,idx):
        answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[3]/a/text()')
        if len(answer) == 0:
            answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[3]/text()')
        return " " if len(answer)==0 else answer[0].replace(",",".")    

    def get_property_3(self, tree,idx):
        answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[5]/a/text()')
        if len(answer) == 0:
            answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[5]/text()')
        return " " if len(answer)==0 else answer[0].replace(",",".")  


    def get_property_4(self, tree,idx):
        answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[7]/a/text()')
        if len(answer) == 0:
            answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[7]/text()')
        return " " if len(answer)==0 else answer[0].replace(",",".")    


    def get_property_5(self, tree,idx):
        answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[9]/a/text()')
        if len(answer) == 0:
            answer = tree.xpath(f'//*[@id="main_table_countries_today"]/tbody[1]/tr[{idx}]/td[9]/text()') 
        return " " if len(answer)==0 else answer[0].replace(",",".")  

