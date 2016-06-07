for i in `seq 300`
do
    python3 scripts/poem.py --source_text data/chat.htm --markov_order 3 > poems/poem_auto_$i.py
done
