def get_search_results():
    while True:
        # GoogleのPC検索結果画面はタイトルをh2でマークアップしている
        for h2_tag in get_h2_tags():
            yield h2_tag
        # 次のページがなくなるまで検索結果を取得し続ける
        if not move_to_next_page():
            break

# get_search_results()
