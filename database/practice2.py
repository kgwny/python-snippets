# SUBSTRなどの関数を使う場合
# SUBSTRなどの関数を使う場合は、SQL()を使用します。

print ('SUBSTRの例')
for r in Pet.select(SQL('SUBSTR(name,1,1)').alias('a1')):
    print (r.a1)

# この例ではname列の1文字目をSUBSTR関数で取得して、それにa1という列名を与えています。

# MAXを使って最大値を取得する場合
# fn.MAXで関数を指定して,クエリーからscalar()を使用して値を取得する。

max = LiveChatMessage.select(
    fn.MAX(LiveChatMessage.offset_time_msec)
).where(LiveChatMessage.video_id  == video_id).scalar()
print(max)
