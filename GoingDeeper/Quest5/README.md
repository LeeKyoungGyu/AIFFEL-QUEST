🔑 **PRT(Peer Review Template)**
코더: 이경규
리뷰어 

- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)** (3/3)
    > 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    > 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
    >    - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부

    1. multiface detection을 위한 widerface 데이터셋의 전처리가 적절히 진행되었다.
      - [x] tfrecord 생성, augmentation, prior box 생성 등의 과정이 정상적으로 진행되었다.
        ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/a9d53716-4c0b-4ca8-b6cf-cafac206847d)
        ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/5c8a7c8b-1135-48fe-ae5f-fbd222b93708)

    3. SSD 모델이 안정적으로 학습되어 multiface detection이 가능해졌다.![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/86e60ec6-fa37-40e2-8f9d-5923fc75fca1)
      - [x] inference를 통해 정확한 위치의 face bounding box를 detect한 결과이미지가 제출되었다.![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/fb65cb7e-f767-4355-b96b-e24049c777a8)
    4. 이미지 속 다수의 얼굴에 스티커가 적용되었다.
      - [x] 이미지 속 다수의 얼굴의 적절한 위치에 스티커가 적용된 결과이미지가 제출되었다.![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/5bb27348-695f-4a34-b3f2-ba8b3908e4fa)


- [ ]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)** (1/3)
    - [ ]  모델 선정 이유 ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/c937ece2-8753-49e7-8bbc-262ac487a244)
    - [ ]  Metrics 선정 이유 ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/f5e0a1d5-c3f6-4a65-82b7-c4d0dd7bfeea) metric은 사용하지 않으셨습니다.
    - [x]  Loss 선정 이유 ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/0fab6556-40a6-46b9-b8f5-68114af5c54a)


- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)** (2/4)
    - [x]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분) ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/7a363219-9f96-4e84-96b5-6e6c9bc9f653)
    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [x]  각 실험을 시각화하여 비교하였나요? ![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/daf6b187-bac8-4d4a-b56d-6cd44c833659)![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/f7a9b6ee-4de9-48a1-9fc8-dc45654f0f5a)![image](https://github.com/hojae-m-choi/AIFFEL-QUEST/assets/98305832/888da9cd-df6e-4579-bc0f-3b5d4cca03c3)
    - [ ]  모든 실험 결과가 기록되었나요?

- [ ]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)** (0/4)
    - 회고를 적지 못하셨습니다.
    - [ ]  배운 점
    - [ ]  아쉬운 점
    - [ ]  느낀 점
    - [ ]  어려웠던 점

#### 리뷰어 회고
짧은 시간에 루브릭을 모두 마쳤습니다. 목표지향적인 접근을 하셨으리라 생각되며 그 점이 인상깊었습니다.
