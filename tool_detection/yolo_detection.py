from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("yolo11m.pt")  

    # 训练模型
    results = model.train(
        data="/localdata/szhoubx/med_video/Motion_VAE/tool_detection/dataset.yaml",
        cfg = "/localdata/szhoubx/med_video/Motion_VAE/tool_detection/config.yaml"
    )
