# test the config
python3 configurator.py   config/train_song_char.py 

# device=mps is Apple Metal (Mac only!)
# was 2000 iterations, now 1000
python3 train.py config/train_song_char.py --device=mps --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=1000 --lr_decay_iters=1000 --dropout=0.0
