# train a miniature song-writing model
# good for debugging and playing on macbooks and such

out_dir = 'out-song-writer'
eval_interval = 250 # keep frequent because we'll overfit
eval_iters = 200
log_interval = 10 # don't print too too often

# we expect to overfit on this small dataset, so only save when val improves
always_save_checkpoint = False

wandb_log = False # override via command line if you like
wandb_project = 'song-writer'
wandb_run_name = 'mini-gpt'

dataset = 'song-writer'
batch_size = 64
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 5000
lr_decay_iters = 5000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially

# on macbook also add
# device = 'cpu'  # run on cpu only. 'mps' is Apple Metal which might be faster - but could only decode on infer via 'cpu' - see https://github.com/pytorch/pytorch/issues/92752
# compile = False # do not torch compile the model
