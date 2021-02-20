# 人別の点数をtupleにしてlistでまとめたオブジェクト
score_list = [('Amen', 50), ('Igor', 79), ('Ursula', 98), ('Eren', 66), ('Olivia', 84)]

score_list.sort(key=lambda x: x[1])

print(score_list)
# [('Amen', 50), ('Eren', 66), ('Igor', 79), ('Olivia', 84), ('Ursula', 98)]
