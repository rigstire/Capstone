from django.db import migrations

# Dictionary mapping model names to new accuracy values
MODEL_ACCURACY_MAPPING = {
"ddrnet23_slim":77.5,
                 "deeplabv3_plus_mobilenet_quantized":68.9,
                 "deeplabv3_plus_mobilenet":72,
                 "deeplabv3_resnet50":78.2,
                 "fastsam_s":74.2,
                 "fastsam_x":76.8,
                 "fcn_resnet50_quantized":72.8,
                 "fcn_resnet50":75.6,
                 "ffnet_40s_quantized":70.3,
                 "ffnet_40s":73.1,
                 "ffnet_54s_quantized":73.9,
                 "ffnet_54s":76.4,
                 "ffnet_78s_lowres":76.1,
                 "ffnet_78s_quantized":75.6,
                 "ffnet_78s":78.2,
                 "ffnet_122ns_lowres":77.5,
                 "hrnet_w48_ocr":81.2,
                 "mask2former":82.7,
                 "mediapipe_selfie":81.0,
                 "pidnet":80.1,
                 "segformer_base":81.5,
                 "sinet":68.3,
                 "unet_segmentation":71.9
}

def update_model_accuracies(apps, schema_editor):
    Benchmark = apps.get_model('benchmark', 'Benchmark')
    AIModel = apps.get_model('aimodels', 'AIModel')
    
    for model_name, new_accuracy in MODEL_ACCURACY_MAPPING.items():
        try:
            ai_model = AIModel.objects.get(name=model_name)
            Benchmark.objects.filter(ai_model=ai_model).update(accuracy=new_accuracy)
            print(f"Updated {Benchmark.objects.filter(ai_model=ai_model).count()} records for {model_name}")
        except AIModel.DoesNotExist:
            print(f"Model {model_name} not found, skipping")

def reverse_update(apps, schema_editor):
    """Optional: Implement if you need to reverse this migration"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        # Update with your actual dependencies
        ('benchmark', '0008_auto_20250420_0102'),
        ('aimodels', '0013_aimodel_qualcomm_link'),
    ]

    operations = [
        migrations.RunPython(
            update_model_accuracies,
            reverse_code=reverse_update
        ),
    ]