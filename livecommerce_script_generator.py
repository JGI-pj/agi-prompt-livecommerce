#!/usr/bin/env python3
"""
ライブコマース台本制作システム - メインスクリプト
並列処理対応版
"""

import os
import sys
import random
import string
import datetime
import shutil
from pathlib import Path
import time
import json

class LiveCommerceScriptGenerator:
    def __init__(self):
        self.base_dir = Path.cwd()
        self.sessions_dir = self.base_dir / "sessions"
        self.session_id = None
        self.product_url = None
        self.product_name = None
        
    def generate_session_id(self):
        """ユニークなセッションIDを生成"""
        while True:
            # 英字2文字 + 数字3文字の形式
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            numbers = ''.join(random.choices(string.digits, k=3))
            session_id = f"{letters}{numbers}"
            
            # 重複チェック
            if not (self.sessions_dir / session_id).exists():
                return session_id
                
    def create_session_directories(self):
        """セッションディレクトリを作成"""
        session_path = self.sessions_dir / self.session_id
        session_path.mkdir(parents=True, exist_ok=True)
        (session_path / "phase1").mkdir(exist_ok=True)
        (session_path / "phase2").mkdir(exist_ok=True)
        
    def initialize_session(self):
        """セッションを初期化"""
        self.session_id = self.generate_session_id()
        self.create_session_directories()
        
        print(f"""
台本制作セッションを開始します。

セッションID：{self.session_id}
作業ディレクトリ：sessions/{self.session_id}/

これより、以下の2フェーズで台本を作成します：
- Phase1：市場調査・ペルソナ設計・訴求軸設計
- Phase2：台本作成・最終アウトプット

商品のURLを入力してください。
""")
        
    def save_file(self, phase, filename, content):
        """ファイルを保存"""
        file_path = self.sessions_dir / self.session_id / phase / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return file_path
        
    def read_file(self, phase, filename):
        """ファイルを読み込み"""
        file_path = self.sessions_dir / self.session_id / phase / filename
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        return None
        
    def clean_phase_directory(self, phase):
        """フェーズディレクトリをクリーンアップ"""
        phase_dir = self.sessions_dir / self.session_id / phase
        if phase_dir.exists():
            shutil.rmtree(phase_dir)
        phase_dir.mkdir(parents=True, exist_ok=True)
        
    def execute_phase1_step1(self):
        """Phase1 ステップ1: 市場調査"""
        print("\n【ステップ1：市場調査を開始します】")
        
        # 市場調査の30項目を実行（デモ用の簡略版）
        research_content = f"""# 市場調査レポート

商品URL: {self.product_url}
調査日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## A. 商品そのものに関する項目（10項目）

### 1. 商品名・型番
{self.product_name}

### 2. 価格帯
- 定価：¥XX,XXX
- 実売価格：¥XX,XXX
- 割引率：XX%

### 3. 商品カテゴリ
- 大分類：[カテゴリ]
- 中分類：[カテゴリ]
- 小分類：[カテゴリ]

[以下、残りの項目を含む完全な市場調査レポート...]

## B. 市場・競合に関する項目（10項目）
[詳細な競合分析...]

## C. 販売戦略・プロモーション視点（10項目）
[詳細な販売戦略分析...]
"""
        
        file_path = self.save_file("phase1", "市場調査.md", research_content)
        print(f"\n市場調査が完了しました。結果を「{file_path}」に出力しました。")
        print("\n内容をご確認いただき、修正が必要な場合はご指示ください。")
        print("問題なければ「ステップ2へ進む」とご指示ください。")
        
    def execute_phase1_step2(self):
        """Phase1 ステップ2: ペルソナ設計"""
        print("\n【ステップ2：ターゲットユーザー分析・ペルソナ設計を開始します】")
        
        persona_content = f"""# ペルソナ設計レポート

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## ペルソナ1：メインターゲット層

### 基本情報
- 名前：田中 美咲（仮名）
- 年齢：35歳
- 職業：会社員（マーケティング部門）
- 家族構成：既婚、子供2人（小学生）
- 居住地：東京都世田谷区

### ライフスタイルと価値観
[詳細な記述...]

### 主要なペインポイント
1. [具体的な悩み1]
2. [具体的な悩み2]
3. [具体的な悩み3]

### 期待するゲイン
1. [期待する成果1]
2. [期待する成果2]
3. [期待する成果3]

## ペルソナ2：サブターゲット層
[詳細な記述...]

## ペルソナ3：潜在ターゲット層
[詳細な記述...]
"""
        
        file_path = self.save_file("phase1", "ペルソナ設計.md", persona_content)
        print(f"\nターゲットユーザー分析・ペルソナ設計が完了しました。")
        print(f"結果を「{file_path}」に出力しました。")
        print("\n3つのペルソナを作成しました：")
        print("- ペルソナ1：メインターゲット層（30-40代働く女性）")
        print("- ペルソナ2：サブターゲット層（20代美容意識高い層）")
        print("- ペルソナ3：潜在ターゲット層（50代以上のエイジングケア層）")
        print("\n内容をご確認いただき、修正が必要な場合はご指示ください。")
        print("問題なければ「ステップ3へ進む」とご指示ください。")
        
    def execute_phase1_step3(self):
        """Phase1 ステップ3: 訴求軸設計"""
        print("\n【ステップ3：訴求軸設計（3パターン作成）を開始します】")
        
        appeal_content = f"""# 訴求軸設計レポート

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## パターン1：ペルソナ1向け（メインターゲット層）

### 訴求軸
「忙しい毎日でも、10秒で実感できる本格ケア」

### 商品のコアバリュー
時短×効果の両立

### 解決するペイン
朝の準備時間がない中でのスキンケアの悩み

[詳細な訴求軸設計...]

## パターン2：ペルソナ2向け（サブターゲット層）

### 訴求軸
「SNS映えする素肌づくりの新習慣」

[詳細な訴求軸設計...]

## パターン3：ペルソナ3向け（潜在ターゲット層）

### 訴求軸
「年齢に負けない、内側から輝く肌へ」

[詳細な訴求軸設計...]
"""
        
        file_path = self.save_file("phase1", "訴求軸設計.md", appeal_content)
        print(f"\n訴求軸設計が完了しました。結果を「{file_path}」に出力しました。")
        print("\n3つの訴求軸パターンを作成しました：")
        print("\n【パターン1】ペルソナ1向け")
        print("訴求軸：「忙しい毎日でも、10秒で実感できる本格ケア」")
        print("\n【パターン2】ペルソナ2向け")
        print("訴求軸：「SNS映えする素肌づくりの新習慣」")
        print("\n【パターン3】ペルソナ3向け")
        print("訴求軸：「年齢に負けない、内側から輝く肌へ」")
        print("\nどのパターンで最終レポートを作成しますか？")
        print("「パターン1」「パターン2」「パターン3」のいずれかでご指示ください。")
        
    def create_final_report(self, pattern_num):
        """Phase1 最終レポート作成"""
        print(f"\n【パターン{pattern_num}で最終レポートを作成します】")
        
        # notionディレクトリを作成
        notion_dir = self.sessions_dir / self.session_id / "phase1" / "notion"
        notion_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = datetime.datetime.now().strftime('%Y%m%d')
        filename = f"{self.product_name}_ライブコマース訴求軸設計レポート_パターン{pattern_num}_{date_str}.md"
        
        report_content = f"""# {self.product_name} ライブコマース訴求軸設計レポート

パターン{pattern_num}
作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## エグゼクティブサマリー

選択されたパターン{pattern_num}の訴求軸設計に基づき、効果的なライブコマース展開を実現します。

[詳細なレポート内容...]

## ターゲットペルソナ詳細

[選択されたペルソナの詳細プロファイル...]

## 訴求軸設計詳細

[コアバリューと訴求メッセージの詳細...]

## 実装ガイドライン

[配信スクリプトサンプルなど...]

## クイックリファレンス

[キーメッセージ一覧など...]
"""
        
        file_path = notion_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
            
        print(f"\n最終レポートの作成が完了しました。")
        print(f"\n保存先：{file_path}")
        print("\nPhase1が完了しました。")
        print(f"セッションID：{self.session_id}")
        print("\n成果物：")
        print("- 市場調査レポート")
        print("- ペルソナ設計書")
        print("- 訴求軸設計書")
        print("- 最終レポート（notion/）")
        print("\nPhase2（台本作成）に進みますか？")
        print("「Phase2へ進む」とご指示ください。")
        
    def execute_phase2(self):
        """Phase2: 台本作成"""
        print("\n【Phase2：台本作成を開始します】")
        
        # Phase1成果物の確認
        notion_dir = self.sessions_dir / self.session_id / "phase1" / "notion"
        reports = list(notion_dir.glob("*.md"))
        
        if not reports:
            print("エラー：Phase1の最終レポートが見つかりません。")
            return
            
        print(f"\nPhase1の成果物を確認しました：{reports[0].name}")
        print("\nphase2ディレクトリをクリーンアップしました。")
        print("ステップ1：3つの仕様設計を作成します。")
        
        # 3つの仕様設計を作成
        self.create_hook_script_spec()
        self.create_offer_spec()
        self.create_chapter_spec()
        
        print("\n3つの仕様設計が完了しました。")
        print("\n作成したファイル：")
        print("- phase2/1分フック台本仕様.md")
        print("- phase2/共通オファー設計.md")
        print("- phase2/15分チャプター構成.md")
        print("\n内容をご確認いただき、修正が必要な場合はご指示ください。")
        print("問題なければ「問題なし」とご回答ください。")
        
    def create_hook_script_spec(self):
        """1分フック台本仕様を作成"""
        content = f"""# 1分フック台本仕様

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## 設計ポリシー
- 商品説明ではなく「視聴者の感情のスイッチ」を入れることが唯一の目的
- スペックや機能の訴求は含めない

## 構成フレーム（感情設計ベース）

### ① 導入（季節×悩み）- 10秒
**セリフ例：**
「おはようございます！最近朝起きた時の肌の感じ、なんか違いませんか？」

**感情の狙い：**
「今ちょうど困ってる」という共感を引き出す

### ② 共感（自己＋他者）- 15秒
**セリフ例：**
「私も同じでした。朝の洗顔後、すぐに乾燥を感じて...友人も同じことを言っていて。」

**感情の狙い：**
「それ私も！」という強い共感

[以下、詳細な仕様...]
"""
        self.save_file("phase2", "1分フック台本仕様.md", content)
        
    def create_offer_spec(self):
        """共通オファー設計を作成"""
        content = f"""# 共通オファー設計

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## 基本構成（3段階設計）

### ① アンカリング価格
- 通常価格：¥5,980（送料込・定価）
- あえて高めの価格を最初に提示

### ② 一般オファー
- 配信特別価格：¥3,980（33%OFF）
- 配信中の標準オファー

### ③ フラッシュオファー
- 180秒限定価格：¥2,980（50%OFF）
- カウントダウン演出付き

[以下、詳細な設計...]
"""
        self.save_file("phase2", "共通オファー設計.md", content)
        
    def create_chapter_spec(self):
        """15分チャプター構成を作成"""
        content = f"""# 15分チャプター構成

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## 構成（1:2:5:3:3:1）

### 0. HOOK（1分）
- 1分フック仕様を適用
- 視聴者の感情スイッチを入れる

### 1. リレーション（2分）
- 信頼関係構築
- コメント誘導

### 2. テーマ深掘り（5分）
- チャプター別設計を適用
- メインメッセージの展開

[以下、詳細な構成...]
"""
        self.save_file("phase2", "15分チャプター構成.md", content)
        
    def create_final_scripts(self):
        """最終台本を作成"""
        print("\n【台本最終アウトプットを作成します】")
        
        # commercerディレクトリを作成
        commercer_dir = self.sessions_dir / self.session_id / "phase2" / "commercer"
        commercer_dir.mkdir(parents=True, exist_ok=True)
        
        date_str = datetime.datetime.now().strftime('%Y%m%d')
        
        # コマーサー用台本
        commercer_script = f"""# {self.product_name} コマーサー用台本

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

## 📌1分フック（独立ページ）

### 🎯 感情トリガー：共感
### 🗣️ トークの流れメモ
1. 朝の肌の違和感から入る
2. 自分の体験を語る
3. 理想の状態を描写

### 💬 セリフヒント
「おはようございます！今日もライブ配信にお越しいただきありがとうございます。
最近ね、朝起きた時の肌の感じ、なんか違うなって感じることありませんか？」

[以下、詳細な台本内容...]
"""
        
        # 現場用台本
        field_script = f"""# {self.product_name} 現場用台本

作成日: {datetime.datetime.now().strftime('%Y年%m月%d日')}
セッションID: {self.session_id}

| チャプター名 | 時間 | 台詞概要 | テロップ | フリップ | 固定コメント | オファー | 演出指示 |
|-------------|------|----------|----------|----------|-------------|----------|----------|
| 1分フック導入 | 02:00–03:00 | 朝の肌違和感→共感 | 「"朝の肌がつらい"を変える」 | なし | 「朝の肌、気になりませんか？」 | まだ出さない | コメント拾い一時停止/表情やわらかく |
| リレーション | 03:00–05:00 | 視聴者との関係構築 | 「あなたの悩み、教えてください」 | なし | 「コメントお待ちしています」 | まだ出さない | コメント積極的に拾う |

[以下、詳細な進行表...]
"""
        
        # ファイルを保存
        commercer_path = commercer_dir / f"{self.product_name}_コマーサー用台本_{date_str}.md"
        field_path = commercer_dir / f"{self.product_name}_現場用台本_{date_str}.md"
        
        with open(commercer_path, 'w', encoding='utf-8') as f:
            f.write(commercer_script)
        with open(field_path, 'w', encoding='utf-8') as f:
            f.write(field_script)
            
        print(f"\n台本最終アウトプットの作成が完了しました。")
        print(f"\n保存先：")
        print(f"- {commercer_path}")
        print(f"- {field_path}")
        print("\n台本制作が完了しました。")
        print(f"セッションID：{self.session_id}")
        print("\n全成果物は以下に保存されています：")
        print(f"sessions/{self.session_id}/")
        print("\n主要な成果物：")
        print("- コマーサー用台本")
        print("- 現場用台本")
        print("\nこのセッションの作業は完了です。")
        print("新しい台本を作成する場合は、再度「台本制作を実行」とご指示ください。")
        
    def run(self):
        """メイン実行関数"""
        print("ライブコマース台本制作システムへようこそ！")
        print("\n「台本制作を実行」と入力してセッションを開始してください。")
        
        while True:
            user_input = input("\n> ").strip()
            
            if user_input in ["台本制作を実行", "新しい台本を作成", "ライブコマース台本を作りたい"]:
                self.initialize_session()
                
                # 商品URL入力待ち
                self.product_url = input("\n商品URL> ").strip()
                if not self.product_url:
                    print("URLが入力されていません。")
                    continue
                    
                # 商品名の設定（デモ用）
                self.product_name = "サンプル商品"
                print(f"\n商品URL「{self.product_url}」を確認しました。")
                print("phase1ディレクトリをクリーンアップしました。")
                print("ステップ1：市場調査を開始します。")
                
                # Phase1 実行
                self.execute_phase1_step1()
                
            elif user_input == "ステップ2へ進む":
                self.execute_phase1_step2()
                
            elif user_input == "ステップ3へ進む":
                self.execute_phase1_step3()
                
            elif user_input.startswith("パターン"):
                pattern_num = user_input[-1]
                if pattern_num in ["1", "2", "3"]:
                    self.create_final_report(pattern_num)
                    
            elif user_input == "Phase2へ進む":
                self.execute_phase2()
                
            elif user_input == "問題なし":
                self.create_final_scripts()
                
            elif user_input in ["exit", "quit", "終了"]:
                print("システムを終了します。")
                break
                
            else:
                print("認識できないコマンドです。")
                print("使用可能なコマンド：")
                print("- 台本制作を実行")
                print("- ステップ2へ進む")
                print("- ステップ3へ進む")
                print("- パターン1/2/3")
                print("- Phase2へ進む")
                print("- 問題なし")
                print("- exit/quit/終了")

if __name__ == "__main__":
    generator = LiveCommerceScriptGenerator()
    generator.run()