CUDA_VISIBLE_DECIVES=1 python lpips_2dirs.py \
-d0 /home/ht1/Xing_tryon/result/TOM/test/try-on \
-d1 /home/ht1/Xing_tryon/data/test/image \
-o ./example_dists.txt \
--use_gpu
# CUDA_VISIBLE_DECIVES=1 python lpips_2imgs.py \
# -p0 /home/data/try-on/cp-vton_Plus/result/TOM/test/try-on/000020_0.jpg \
# -p1 /home/data/try-on/cp-vton_Plus/result/GMM/test/overlayed_TPS/000020_0.jpg \
# --use_gpu
