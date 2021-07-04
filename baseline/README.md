#  task03-rank03-team_SKKU_COMEDU

### 1. Submission File에 대한 Description
최종 제출 파일인 submission.zip 파일을 아래의 경로 형태로 설정
```
$(DATA)
|-- Final_DATA
|   |-- task03_train
|   |-- task03_test
|
|-- submission
|   |-- baseline
|-- submission.zip
```


### 2.  Code File에 대한 Description
```
$(baseline)
|-- data				
|-- models
|-- runs
|-- utils
|-- preprocess.py
|-- test.py
|-- train.py
|-- train1.py
|-- train2.py 
```

- ```data``` : 하이퍼 파라미터 관련 정보를 담은 폴더
- ```models``` : YOLOv5 모델 정보에 대한 yaml 파일 폴더
- ```runs``` : train 결과(경로: ```runs/train/```)와 test 결과(경로: ```runs/test/```)가 저장되는 폴더
- ```utils``` : train과 test에서 사용되는 여러 함수들을 모아 둔 파이썬 코드 폴더
- ```preprocess.py``` : 학습 전 데이터 라벨링을 위한 전처리 코드 
- ```test.py``` : 테스트를 위한 파이썬 코드
- ```train.py``` : train1.py과 train2.py를 한 번에 실행하는 파이썬 코드
- ```train1.py``` : model1 train하는 파이썬 코드
- ```train2.py``` : model2 train하는 파이썬 코드

### 3. Output에 대한 Description
```
$ (baseline)
|-- runs
|   |-- test
|   |	|-- output
|   |	|   |-- best_prediction.json
|   |
|   |-- train
|   |	|-- model1
|   |	|   |-- weights
|   |	|   |	|-- best.pt
|   |	|   |	|-- last.pt
|   |   |
|   |	|-- model2
|   |	|   |-- best_prediction.json
|   |	|   |   |-- best.pt
|   |	|   |   |-- last.pt
```
- ```best_prediction.json``` : json 결과 파일 
- ```best.pt``` : best train weights 파일 (default)
- ```last.pt``` : last epoch train weights 파일
- Result Report (경로: ```baseline/runs/train/model*/```)
	1. ```F1_curve, PR_curve, P_curve, R_curve``` : F1, PR, P, R curve 이미지 파일
	2. ```Result.txt``` : 학습 정보 텍스트 파일
	3. ```confusion_matrix.png```  : Confusion Matrix 시각화 이미지 파일
	4. ```result.png``` : 학습 결과 시각화 이미지 파일
	5. ```etc.``` : 외 여러 시각화 정보 파일


### 4. 학습에 필요한 명령어
```bash
$ python3 train.py
```

### 5. 테스트에 필요한 명령어
```bash
$ python3 test.py
```

## Tutorial

### 전체 실행 순서 
```
Unzip -> Install requirements -> Change directory -> Prepocess -> Train -> Test 
```
###  1. Unzip
```bash
$ unzip submission.zip
$ cd submission
```
### 2. Install Requirements
```bash
$ pip install -r requirements.txt
```
### 3. Change directory
```bash
$ cd baseline
```
### 4. Preprocess
```bash
$ python3 preprocess.py
```
- preprocess.py : 학습 전 데이터 라벨링을 위한 전처리 코드
- 재현 서버에서 약 40분 소요
- 라벨 저장 경로 : ```/DATA/Final_DATA/task03_train/labels/*.txt```
- 총 273,224 텍스트 파일 

### 5. Train
```bash
$ python3 train.py
```
- ```train.py``` : ```train1.py``` (model 1)와 ```train2.py``` (model 2)를 순서대로 한 번에 실행하는 코드
- 총 55 epoch (model 1 : 30 epoch, model 2 : 25 epoch)
- 재현 서버에서 총 약 9시간 소요
- 학습 후 2개의 weight 파일 생성
```baseline/runs/train/model1/weights/best.pt``` 
```baseline/runs/train/model2/weights/best.pt```

**주의사항** : train이 중간에 중단된 경우  혹은 새로운 train을 다시 시작하려 할 경우, 아래를 실행하고 다시 학습 진행해야 함
```bash
$ rm -r runs/train
```
이는 ```test.py``` 실행 시 앙상블을 하기 위한 2개의 weights 파일의 경로의 default가 아래와 같이 지정되어 있기 때문
```python
parser.add_argument('--weights', nargs='+', type=str, default=['runs/train/model2/weights/best.pt', 'runs/train/model1/weights/best.pt'], help='model.pt path(s)')
```

### 6. Test
```bash
$ python3 test.py 
```
- ```test.py``` : 테스트를 위한 코드
- model 1과 model 2 각각의 weight 파일으로 앙상블 테스트 실행
- 결과 json 파일 생성 (경로 : ```runs/test/output/best_prediction.json```)

