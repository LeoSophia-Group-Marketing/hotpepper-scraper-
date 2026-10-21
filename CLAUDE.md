# 広告・GA・hacomono データ取得の共通ルール（the SILK / TADASU）

伊藤さん（LeoSophia / HYV）の広告分析で使う、データ取得と集計のルール。
データは Supermetrics MCP 経由で取得する。（2026-10-21 時点）

## アカウント

- **GA4（GAWA）**
  - the SILK: 342354930
  - the SILK_物販: 511761151
  - TADASU整体: 463727943
  - Olive pilates: 512781074
- **Meta（FA）**
  - the SILK 自社: act_315332727138516（アカウント時間は America/Los_Angeles）
  - 他社運用（キャンペーン名が SY_、広告ID末尾 …0005）は Supermetrics の優先アカウント上限で取得できない。
    コストは共有シート「the SILK Meta配信実績_共有用」（1ouIFUqNOqJFUoqIGXezlcnWR9x8bS_T9hc7GmmJxODc）の daily集計シート C列を使う。
  - Supermetrics の優先アカウントは、伊藤さんの許可なく変更しない。
- **Google広告（AW）**
  - the SILK: 4750803500（株式会社HYV）
  - TADASU整体: 4956425872（LSSD_整体）
  - Olive: 2654365393

## hacomono CV（= GA CV）の数え方

- hacomono の予約完了は GA4 で計測している。
  - the SILK: イベント `reservation_complete`（reserve.the-silk.co.jp）
  - TADASU: イベント `reserve`（2026年5月以前は「体験予約」）
- TADASU の `reserve` はメール確認完了ページ（/mypage/mail-address-confirm/complete）でも誤発火する。/reserve/complete/trial のページだけを数える。
- 予約IDの重複は必ず除く。pageLocation（または pagePath）の reservationId を使い、同じIDは最初に出た日だけ数える。
- the SILK では、6桁以下の短い予約IDは不正として除外する（2025-11-24以降、SY_ アカウント経由で多発）。
- 過去の予約完了ページを開き直しただけのアクセスも混ざる。その日の予約IDの中央値の97%未満の古いIDは除外する。
- 長い期間を pageReferrer などの細かい項目付きで1回で取ると、GA4 が行を間引いて件数が欠ける。8日以内に分けて取得し、結合してから重複を除く。
- GA4 のディメンションは1クエリ9個まで。
- 当日分のGAは数時間遅れて反映されるので、「暫定」と明記する。

## Meta 広告と GA CV の紐づけ

- 自社アカウントの UTM:
  - utm_campaign = `campaign_id_{キャンペーンID}_adset_id_{広告セットID}_ad_id_{広告ID}`
  - utm_content = 広告ID
  - source / medium = `meta / display`
- sessionCampaignName を「campaign_id」を含むで絞り、IDで突き合わせる。
- utm_content が (not set) で、表示のない広告も含めて全広告に一律4〜7セッション入っている場合は、広告作成直後の審査ボットなどの自動アクセスとみなす。CVR の分母から外す。
- パーソナルの CV は、pageReferrer の itemCode=I0616、またはスタジオID 76〜79（79 新宿、78 目黒、77 横浜）で判定する。

## Meta のコストを日本時間に換算する

- Meta のコストはアカウント時間（米国太平洋時間）で区切られている。
- 日本時間で集計するときは `hourly_stats_aggregated_by_advertiser_time_zone` で時間別に取得し、+16時間（夏時間中）ずらして合計する。
- 日本時間の1日 = 太平洋時間の前日 8:00〜当日 7:59。

## 店舗の特定（the SILK）

- 予約完了の pageReferrer にある /reserve/space/{スペースコード}/ を、スタジオIDに変換する。
  - 変換表は、/reserve/space/{コード} のページに /reserve/schedule/{スタジオID}/… から来た遷移を集計して作る。
- スタジオIDと店舗名の対応は、店舗ページ /studios/… から /reserve/schedule/{ID}/ へのリンククリック（linkUrl）で取れる。
  - 例: 1 広尾、10 銀座、11 新宿、13 横浜、34 松戸、47 所沢、61 高田馬場、62 心斎橋、64 巣鴨、66 秋葉原、67 浅草

## 報告のルール

- CPA・CVR は重複を除いた GA CV で出す。媒体の管理画面の CV は参考扱い。
  - 例: TADASU の Google広告の CV は実数の約2.8倍に膨らんでいた。
- 集計条件を必ず書く（期間、日本時間かどうか、重複除外の有無、暫定値かどうか）。
- 会員の住所などの個人情報は作らず、慎重に扱う。
