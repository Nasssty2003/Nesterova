Tests
![Снимок экрана 2022-12-16 в 00 43 36](https://user-images.githubusercontent.com/43472988/207952542-8e647532-1c7e-4bda-a0d3-0872d791ceb9.png)
![Снимок экрана 2022-12-16 в 00 43 53](https://user-images.githubusercontent.com/43472988/207952564-de16b2dd-c5a3-4908-93f4-01ba0c92434f.png)

Profiling

Измерим время выполнения программы и найдём самую времязатратную функцию


![205325739-8709b4a1-fbc5-47a1-b4b9-3e5d4c783991](https://user-images.githubusercontent.com/43472988/208233342-b73f4646-1380-467d-8d5f-7d283b23bb0a.png)
![22222](https://user-images.githubusercontent.com/43472988/208233347-55316086-f4df-44a1-ad2a-536abe62e945.png)

Пишем другие варианты реализации функции
1)
![123](https://user-images.githubusercontent.com/43472988/208233522-1c9f316c-3865-4f0b-bb13-5ba760ecf9ab.png)
![ешьу](https://user-images.githubusercontent.com/43472988/208233466-0dae7319-0a05-4e54-b84c-f48a2cd6fd29.png)

2)
![2а](https://user-images.githubusercontent.com/43472988/208233465-c60301d1-a743-445b-9af1-d74ff67430a9.png)
![time_a](https://user-images.githubusercontent.com/43472988/208233502-a1362ca6-a914-4155-8a96-35b7a8afb438.png)

3)
![3f](https://user-images.githubusercontent.com/43472988/208233488-390d772e-cd2b-4a8c-b4c1-b71a012cd142.png)
![time3](https://user-images.githubusercontent.com/43472988/208233497-746aa124-185f-40a6-af96-daf77dc7cdba.png)

Сравниваем время выполнения и выясняем, что последний вариант самый эффективный

3.2.1

![3 2 1](https://user-images.githubusercontent.com/43472988/208263370-8a6c6e66-ee93-48fb-b738-2477d07412bd.jpg)

3.2.2

Результаты работы скрипта без многопроцессорной обработки:

![агт](https://user-images.githubusercontent.com/43472988/208510120-11939c8a-c382-4b29-9e75-72e2ef59e635.png)

Результаты работы скрипта с многопроцессорной обработки:

![агн2](https://user-images.githubusercontent.com/43472988/208510172-bb4c8eee-ea49-488a-97a5-a1098abe8d72.png)

