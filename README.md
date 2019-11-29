# VideoSuperResolution
AI+4K HDR competition from Kesci Community

## 模型文件

* 136000 https://share.weiyun.com/5ouNypV
* 280000 https://share.weiyun.com/5qX9n5X
* meta_info.pkl https://share.weiyun.com/5afpxKj

## 项目的文件结构

- codes
  - test.py
  - test_HDR.py
  - test_HDR_woGT.py
  - train.py
  - data
  - metrics
  - models
  - options
  - scripts
  - utils
- experiments
  - 模型文件
- results
  - 保存图片的路径

## 项目的运行步骤

### 训练模型

```
cd codes
python -m torch.distributed.launch --nproc_per_node=8 --master_port=4321 train.py -opt options/train/train_EDVR_L2.yml --launcher pytorch
```

**train_EDVR_L2.yml**为配置文件，需要修改meta_info.pkl、图片路径、预训练模型路径。

- 模型文件放置在 `../experiments/pretrained_models/136000_G.pth`



### 测试模型

2. 运行测试脚本，生成图片

   ```
   cd codes
   # 需要注意修改模型路径和图片路径，该脚本是跑8张卡，省时间，可以改为1张卡跑完
   ./run_test_woGT.sh
   ```

3. 在results文件夹中含有生成的结果



### 生成视频

```
# 修改脚本中的图片结果路径和视频生成路径
cd results
python convert_to_h265.py
```



## 运行结果的位置

../results/HDR/test/test_128_wTSA/HDR/

可自定义