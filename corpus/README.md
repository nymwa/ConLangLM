# corpus

## tatoeba

用意するためにはtatoebaのDownloads ( https://tatoeba.org/eng/downloads ) からダウンロードするスクリプトdownload.shを実行してください．

トークナイズは以下のコマンドで行ってください．
```
cut -f 3 toki_sentences.tsv | tokipona-tokenize --replace-proper-noun --remove-sentence-with-unk > tatoeba_tokenized.txt
```

## tokipona1000

raw.txtが生コーパスです．

tokenized.txtがトークナイズ済コーパスです．
`tokipona-tokenize < raw.txt > tokenized.txt` で生成できます．

proper_noun_replaced.txtが固有名詞を`<proper>'に置き換えたトークナイズ済コーパスです．
`tokipona-tokenize --replace-proper-noun < raw.txt > proper_noun_replaced.txt` で生成できます． 



