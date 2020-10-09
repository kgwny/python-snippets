# 文字列表現を短縮するパラメータつきデコレータ
def parametrized_short_repr(max_width=8):

    # 実際のデコレータとして使用される内部ラッパー関数
    def parametrized(cls):

        # デコレートされた動作を提供するサブクラス
        class ShortlyRepresented(cls):

            def __repr__(self):
                return super().__repr__()[:max_width]

        return ShortlyRepresented

    return parametrized

@parametrized_short_repr(8)
class ClassWithLittleBitLongerLongName:
    pass

# デコレートされた動作を提供するサブクラス
ClassWithLittleBitLongerLongName().__doc__
