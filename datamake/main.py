from collections import defaultdict
from paddleocr import PaddleOCR

from sklearn.model_selection import train_test_split


import re
def parser_core_data(ocr_data):
    ocr_data=ocr_data[0]
    BBOX_INDEX=0
    TEXT_SCORE_INDEX=1
    TEXT_INDEX=0
    company_full_name_pattern=re.compile(r"(?P<full_name>^.*有限公司)",re.DOTALL)
    company_short_name_pattern=re.compile(r"(股票|公司|证券)简称(:|：)(?P<short_name>.*)($|公司|证券)",re.DOTALL)
    company_code_name_pattern=re.compile(r"(股票|公司|证券)代码(:|：)(?P<code_name>\d+.\d+$)",re.DOTALL)
    info_dict=defaultdict(set)
    for span_data in ocr_data:
        text=span_data[TEXT_SCORE_INDEX][TEXT_INDEX]
        match=company_full_name_pattern.search(text)
        if match:
            info_dict["full_name"].add(match.groupdict()["full_name"])
        match=company_short_name_pattern.search(text)
        if match:
            short_name=match.groupdict()["short_name"]
            for sn in re.split("、| ",short_name):
                info_dict["short_name"].add(sn)
        match=company_code_name_pattern.search(text)
        if match:
            code_name=match.groupdict()["code_name"]
            for cn in re.split("、| ",code_name):
                info_dict["code_name"].add(cn)
    return info_dict
    
    

def pipeline01():
    pass

from glob import glob 
import shutil,os 
import json
from tqdm import tqdm
basic_image_dir="dataset/images"
# for image_path in glob("/media/liukun/7764-4284/cninfo/CnInfoReports/pdfs/ndbg_zy_images/*/*-1.png"):
#     #print(image_path)
#     file_name=image_path.split("/")[-1]
#     if os.path.exists(f"{basic_image_dir}/{file_name}"):
#         continue
#         os.remove(f"{basic_image_dir}/{file_name}")
#     shutil.copy2(image_path,f"{basic_image_dir}/{file_name}")

def dump_jsonl(data_list,data_path):
    with open(data_path,"w") as df:
        for  data in data_list:
            json.dump(data,df,ensure_ascii=False)
            df.write("\n")
def batch_infer_images():
    """
    批量ocr图片
    """
    paddleocr = PaddleOCR(
        det=True,
        rec=True,
        lang="ch",
        #lang="ch",
        cls=True,
        use_gpu=True,
        show_log=False,
        use_space_char=True
        
    )
    def ocr_infer_image(image_path):
        ret_data=paddleocr.ocr(image_path)
        return ret_data
    for image_path in tqdm(glob(f"{basic_image_dir}/600843*.png")):
        file_name=image_path.split("/")[-1]
        prefix_file_name,ext=os.path.splitext(file_name)
        os.path.split(file_name)
        ocrdata=ocr_infer_image(image_path)
        with open(f"{basic_image_dir}/{prefix_file_name}.json","w") as jsonfile:
            # ocr数据。
            json.dump(ocrdata,jsonfile,ensure_ascii=False)
def batch_parser_ocr_data():
    #批量解析ocr数据
    c=0
    all_gt_docunt_data=[]
    for json_path in tqdm(glob(f"{basic_image_dir}/*.json")):
        file_name=json_path.split("/")[-1]
        prefix_file_name,ext=os.path.splitext(file_name)
        with open(json_path,"r") as jsonfile:
            ocr_data=json.load(jsonfile)
            info_dict=parser_core_data(ocr_data)
            if len(info_dict["full_name"])!=1:
                c=c+1
                continue
            if len(info_dict["short_name"])==0 or len(info_dict["code_name"])==0:
                # print(ocr_data)
                # print(info_dict)
                c=c+1
                continue
            gt_docunt_data=defaultdict(list)
            for key_name,values in info_dict.items():
                for v in values:
                    gt_docunt_data[key_name].append({f"{key_name[0]}n":v})
            image_path=f"{prefix_file_name}.png"
        all_gt_docunt_data.append(
            {
                "ground_truth":json.dumps({"gt_parse":gt_docunt_data},ensure_ascii=False),
                "file_name":image_path
            }
        )
    train_data,test_data=train_test_split(all_gt_docunt_data,test_size= 0.3,shuffle=True,random_state=22)
    import shutil
    for d in train_data:
        os.makedirs(f"{basic_image_dir}/train",exist_ok=True)
        shutil.copy2(f"{basic_image_dir}/{d['file_name']}",f"{basic_image_dir}/train")
    for d in test_data:
        os.makedirs(f"{basic_image_dir}/val",exist_ok=True)
        shutil.copy2(f"{basic_image_dir}/{d['file_name']}",f"{basic_image_dir}/val")        
    print(len(train_data),len(test_data))
    dump_jsonl(train_data,f"{basic_image_dir}/train/metadata.jsonl")
    dump_jsonl(test_data,f"{basic_image_dir}/val/metadata.jsonl")
    

    print(c,len(glob(f"{basic_image_dir}/*.json")))
    #parser_core_data(ocrdata)
    #print(ocrdata)
batch_infer_images()
batch_parser_ocr_data()