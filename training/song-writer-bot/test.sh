# device=mps is Apple Metal (Mac only!) but could only decode on infer via 'cpu' - see https://github.com/pytorch/pytorch/issues/92752
python3 sample.py --out_dir=out-song-writer --device=cpu --start="Death"

ls out-song-writer
