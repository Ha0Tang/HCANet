CUDA_VISIBLE_DEVICES=0;
python train.py --name TOM --stage TOM --workers 8 --save_count 5000 --shuffle -b 4
