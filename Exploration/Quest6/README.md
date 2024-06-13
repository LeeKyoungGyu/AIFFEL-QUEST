### 06.13. 피어 코드 리뷰
***
### 코더 : 이경규님
### 리뷰어 : 고대현
***
### 총평
이번 실습 및 프로젝트에서 시간도 오래 걸리고 생각보다 해야 할 것도 많았었는데,

시간 안에 많은 실험과 그 안에서 인사이트를 찾으셨고, 설명도 잘 해주셔서 좋았습니다 :)

경규님 고생하셨습니다!

🔑 **PRT(Peer Review Template)**

- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
    - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부
![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/45a354b2-ba1a-44f9-87f3-e2f8b20c2ec5)
1) 분석단계, 정제단계, 정규화와 불용어 제거, 데이터셋 분리, 인코딩 과정이 빠짐없이 체계적으로 진행되었다.
> 모든 과정을 순서 및 흐름을 살려 실험을 체계적으로 진행해주셨습니다.
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/9b48da7a-5ebf-43b9-982b-3cf1a6933771)
2) 모델 학습이 진행되면서 train loss와 validation loss가 감소하는 경향을 그래프를 통해 확인했으며, 실제 요약문에 있는 핵심 단어들이 요약 문장 안에 포함되었다.
> 모델 학습이 진행되면서 train loss와 validation loss가 감소하는 경향을 그래프를 통해 확인하셨습니다.
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/3f6851fd-554d-4b14-9a69-2dd08d7a6f51)
3) 두 요약 결과를 문법 완성도 측면과 핵심단어 포함 측면으로 나누어 비교하고 분석 결과를 표로 정리하여 제시하였다.
> 문법 완성도 측면과 핵심단어 포함 측면으로 나누어 비교하고 분석 결과를 표로 정리하여 제시하셨습니다.
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/480871f2-a45c-4461-9e3b-074c70e4bf70)

- [ ]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
> 모델, Metrics, Loss 모두 잘 이용해주셨지만, 사용하신 이유에 대해서는 주석 혹은 마크다운 언어로 설명하시지 않으셨습니다.
    - [ ]  모델 선정 이유
    - [ ]  Metrics 선정 이유
    - [ ]  Loss 선정 이유

- [X]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [X]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
> 데이터를 분할하여 프로젝트를 진행하셨습니다. (train, test 8:2 구분)
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/66482ea8-7506-4abc-be8c-334b19c09be8)
    - [X]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
> 에포크 수와 early stopping 등을 사용하시며 실험을 진행해주셨습니다.
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/e5f3cf8b-fbc3-43a1-8354-0d355cb55325)
    - [X]  각 실험을 시각화하여 비교하였나요?
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/6c0e65d2-b77d-409b-888c-13d2c3d589ac)
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/f4ee904c-5071-4fdb-9734-3f7c8740e7eb)
> 각 실험을 시각화하여 비교하셨습니다.
    - [X]  모든 실험 결과가 기록되었나요?
> 모든 실험 결과가 기록되었습니다. 위의 사진으로 갈음합니다.

- [X]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
> ![image](https://github.com/LeeKyoungGyu/AIFFEL-QUEST/assets/102419537/14a1a262-44d6-4be1-afa2-915fa9b5f518)
    - [X]  배운 점 : "회고록 중 / 추상적요약과 추출적요약의 차이에 대해 알 수 있었다."
    - [X]  아쉬운 점 : "회고록 중 / 모델 학습 시간이 오래걸렸다."
    - [X]  느낀 점 : "회고록 중 / 어렵게만 생각했던 요약을 seq2seq과 summa로 풀 수 있는 점이 놀라웠다."
    - [X]  어려웠던 점 : "회고록 중 / 모델의 세부 인자, 파라미터에 대해 더 공부해야겠다."
