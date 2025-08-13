items = []                        #グローバル変数（関数内外とも使用可）,空の配列（関数により空配列に要素を追加する）　配列＝リスト

class ListEditor:                 #関数内で定義する変数はローカル変数となり、関数内でしか使用できない,:を忘れない
    def add_item(self,item):      #pythonの引数にはself（第一引数）が必須,:を忘れない
        items.append(item)        #appendは配列に要素を追加する

    def remove_item(self, item):
        items.remove(item)        #removeは配列の要素を削除する


listeditor = ListEditor()         #空のインスタンス生成
item = "ペン"                     
listeditor.add_item(item)         ##インスタンスに値を代入

item = "消しゴム"
listeditor.add_item(item)

item = "パソコン"
listeditor.add_item(item)

listeditor.remove_item(item)
print(items)



""" class クラス名:
    変数名 = 値                 #クラス変数
    def メソッド名(self, 引数):  #クラス内のメソッドにはselfが必須
        処理
    def メソッド名(self, 引数):
        処理
        
インスタンス名 = クラス名(引数1, 引数2) #インスタンスの生成
インスタンス.メソッド名(引数1, 引数2)
インスタンス.インスタンス変数名
インスタンス.クラス変数名
"""