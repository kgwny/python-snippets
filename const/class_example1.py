# 定数クラスを呼び出すクラス
import const

const.IKA = 'ika'
const.HOGE = 'hoge'
print(const.IKA)
print(const.HOGE)

# const.IKA = 'TAKO'
# const.ConstError: Can't rebind const (IKA)
# 上書き不可
