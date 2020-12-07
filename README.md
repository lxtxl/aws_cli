# aws_cli란?
1. aws cli 명령어를 쓰다 보니, 기능이 너무 많이 생성이 되고, 그것들을 aws cli reference 사이트를 찾아가면서 찾다 보니 너무 힘들어, reference 사이트의 내용을 가져다, 디렉토리/파일명으로 쉽게 쓸수 있게 하기 위해 만듬

# 설치 요구사항
1. python 3.x 사용
2. awscli 2.x 설치되어 있어야 함

# 사용 방법
## config 세팅
1. setting.json 세팅 ( 프록시를 사용하는 환경과 아닌 환경에 따라서 ) 
```
config/setting_no_proxy.json.sample => config/setting.json
or
config/setting_proxy.json.sample => config/setting.json 
```

2. 여러 profile을 지원해야 하기 때문에 아래와 같이 profile 세팅을 해야 함 ( aws cli의 profile 세팅 )
```
config/project_name.json_sample 
    => config/innotree.json
    => config/mine.json

{
    "profile": "<<aws_cli의 profile>>",
    "region": "<<region 명칭>>",
	  "output": "table",
    "owner_id": "xxxxxxx",
    "vpc_id": "vpc-xxxxxxxxxx"
}

owner_id 와 vpc_id 는 특정 범위를 지정하는 command에 사용됨
```

## 파라미터가 없는 명령어 실행
```
python ec2_read/instance_list.py innotree

innotree 프로젝트의 ec2 서비스의 instance 목록을 보고 싶다
```
## 파라미터가 하나 있는 명령어 실행
```
python ec2_read_1/instance_get.py innotree <<instance_id>>
```

## 명령어에 대해서 결과 내용이 result_YYYYMMDD 폴더에 파일이 생성이 된다.
```
HHMMSS_<project_name>>_ec2_describe_instances.text 로 생성
```

## 여러 파라미터가 있는 경우 generate 파일 생성을 위해서는 프로젝트명 대신에 gen을 넣으면 파일이 생성함
python ec2_write/vpc_create.py gen

## ec2 정보 가져오기
ls -al | awk '{print $9}' > ../get_ec2.sh

## custom 항목 만들기

## setting.json에 있는 인자를 사용해서 읽기
1. list 파일 내용을 복사해서 새로 만들기
```angular2html
cp ec2_list/subnet_list.py subnet_list_in_vpcid_.py

옵션을 아래와 같은 형태로 넣기 (치환할 것은 $$로 )
add_option_dict["setting_matching_parameter"] = "--filters \"Name=vpc-id,Values=$$\""
add_option_dict["setting_key"] = "vpc_id"

add_option_dict["setting_matching_parameter"] = "--owners $$"
add_option_dict["setting_key"] = "owner_id"
```
# 내가 바라는 것
1. 명령어를 쉽게 쓸수 있어야 한다.
2. 명령어에 대해서 결과를 이력에 남겨야 한다.
3. 스크립트 파일은 AWS CLI Reference 에 추가되면 쉽게 추가를 할수 있어야 한다.
