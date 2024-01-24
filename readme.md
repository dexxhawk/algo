## Содержание:
* Тренировки 2.0:
  1. Линейный поиск
  2. Множества
  3. Словари и сортировка подсчетом
  4. Префиксные суммы
  5. Два указателя
  6. Бинарный поиск
  7. Сортировка событий
  8. Бинарные деревья
___
* Тренировки 3.0:
  1. Стеки
  2. Очереди, Деки, Бинарные кучи и Приоритетные очереди 
  3. Одномерное ДП
  4. Двумерное ДП, ДП по подотрезкам
  5. DFS
  6. BFS
___
* Дополнительные материалы:
  * Will be soon...

## DFS (обход в глубину)
**Применение:** обход графов, проверка на связность, поиск КС, поиск цикла, проверка на двудольность, топсорт.

В DFS, как только мы нашли соседа вершины, сразу идем в него.

<details>
<summary>Общие моменты:</summary>

**Дерево** - связный (сущ. пусть от каждой вершины до каждой) ациклический граф, `кол-во ребер = кол-во вершин - 1`.

**Полный граф** - каждая вершина соединена с каждой, количество ребер = `V(V - 1).`

**Двудольный граф** - все вершины можно разложить по 2 долям, и ребра будут только между вершинами из разных долей

**Графы,** в которых кол-во ребер сильно меньше V^2 наз. **разрежеными** (V^3/2. Если меньше, то точно не подходит матрица смежности за исключением очень маленьких задач)\
Основные **способы хранения** графов в задачах:
1) Матрица смежности - `O(V^2)` памяти и времени  
2) Список смежности - `O(V + E)` памяти и времени

Почти всегда в задачах нужно уметь по номеру вершины определить номера всех ее соседей.
Порядок обработки обычно не имеет значения.

**КС** - (максимальное по включению) подмножество вершин и ребер их соединяющих, внутри которого можно дойти от каждой вершины до каждой и его нельзя расширить (нельзя добавить вершины) 
**КС и Связность** только для НЕОРГРАФА.\

### Код:
```py
def dfs(graph, visited, now):
  visited[now] = True
  for neig in graph[now]:
    if not visited[neig]:
      dfs(graph, visited, neig)
```
<details>
<summary>Задачи:</summary>

---

**Проверка на связность** - запускаем DFS и считаем кол-во вершин
 
 В этой и дальнейших задачах граф может иметь несколько компонент связности, поэтому чтобы пройтись по всем вершинам, перебираем все вершины:
 ```py
 for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, visited, i)
 ```
---

### Поиск цикла
***Идея*** - пометка в белый, серый, черный\
В момент запуска DFS в стеке находятся вершины, обязательно лежащие на каком-то ПУТИ. Если метить их в 3 цвета, то все вершины, лежащие на этом пути(и никакие другие) будут помечены серым.\
Черным метим вершину, когда посетили всех соседей, т.е. все достижимые вершины просмотрены. Для всех вершин, которые из нее достижимы, цикла нет, и когда мы находим новый путь в черную вершину, от этого гарантированно цикла не образуется


(в неорграфе надо таскать с собой номер предка и игнорировать покраску предка серым. Если придем до предка серого каким-то другим путем, то цикл будет.)

</details>

</details>

## BFS (обход в ширину, волновой алгоритм)
**Применение:** определение кратчайших путей в невзвешенных / 0-1 графах, обход графов.

DFS находит какой-то путь, BFS находит кратчайший.

Делается с помощью *очереди* / *списков вершин, находящихся на заданном расстоянии*
(В худшем случае обе реализации дают одинаковую сложность по памяти и времени `O(V+E)`, мы будем использовать очередь)
![bfs1](/img/bfs1.jpg)
![bfs1](/img/bfs2.jpg)

**Основной алгоритм:** Помещаем в очередь стартовую вершину, пока очередь не пуста удаляем вершину из очереди и смотрим ее соседей.


(На k-ом шаге в очереди будут только элементы с расстояниями K и K +1
Когда обработали все вершины, находящиеся на расстоянии k, мы нашли и положили в очередь все вершины, находящиеся на расстоянии k + 1)
```py
queue.add(start)
while not queue.empty():
    now = queue.get()
    for neig in graph[now]:
        if dist[neig] == -1:
            dist[neig] = dist[now] + 1
            queue.append(neig)
print(dist[end])
```

+ ***1 начало, много концов:***
Выбираем минимум среди всех конечных

+ ***Много начал, 1 конец:***
"Разворачиваем" задачу. Если был орграф, то разворачиваем еще и ребра. 

+ ***Много начал, много концов:***
Несколько вершин помечаем 0(расстоние до них) и сразу добавляем их в очередь
Среди конечных выбираем минимум

![bfs3](/img/bfs3.jpg)
Для восстановления ответа используем массив *prev*. Без prev пришлось бы ребра разворачивать...
Либо идем по табличке в клетку, где расстояние на 1 меньше, но работает только с орграфом

<details>
<summary>Задачи</summary>

**1. Для каждой вершины(ребра) графа определить, находится ли это вершина(ребро) на каком - либо кратчайшем пути от А до B.**

**Вершины:**

*Неорграф:*
Делаем 2 обхода в ширину: от A в B и от B в A. `Расстояние от A до вершины + От B до вершины = длине кратчайшего пути` => вершина лежит на пути

*Орграф:*
Разворачиваем ребра перед вторым обходом.

![bfs4](/img/bfs4.jpg)
**Ребра:**

Если оба конца лежат на кратчайшем пути, то лежит, но нужна проверка:
1) `различны расстояния для A`
2) `x + y = k - 1`, где
x - расст от A до начала ребра, y - расст от конца ребра до B
тк должны быть на пути k - 1 ребро + 1 наше, которое мы проверяем

Аккуратно с ориентированными ребрами


---

**2. Кратчайший путь в очень большом графе (например, соцсети)**
![bfs5](/img/bfs5.jpg)

**АЛГОРИТМ:**
Найдем все вершины, находящиеся на расстоянии 1 от A, 1 от B. Если пересечение этих 2 множеств не пусто, есть путь, иначе делаем еще по шагу.
Как только пересечение не пусто - можем построить цепочку.
Восстанавливаем левую часть пути от текущей вершины(любая, которая в пересечении) , правую часть от вершины до конца, склеиваем и получаем полный кратчайший путь

Этот способ в ряде случаев для очень больших графов позволяет быстро находить кратчайший путь. (Не факт, что два BFS дойдут до O(V), до некоторых вершин можем вообще не дойти).
Но это имеет смысл, только если очень большой граф и медленный способ получения соседей, когда попытка запустить обычный обход в ширину быстро достигает (шагов за 6, например) V. Здесь же есть шанс, что не придется даже хранить весь граф (напр., соцсети).

(В случае полного графа решение не за const, а за размер размер графа - надо как-то считать в память его. Чтобы проверить, что граф полный - надо посмотреть на все вершины, все ребра и что-то предпринять)
___
**3. Граф состояний**
![bfs6](/img/bfs6.jpg)

<details>
<summary>До конца не понял, но вот записи:</summary>
Есть 2 машинки, надо поменять их местами.\
Эл. действие - переезд 1-ой машинки\
Состояние - пара из позиций 2 машин\
Для этого графа ребра в явном виде строить не нужно.\
Поиск соседей не обязательно делается за счет того, что мы перебираем ребра в текущем графе, мы перебираем в исходном графе такие ребра
Можно объединить 2 идеи и поиск делать так, как в большом графе, тк нам нужно попасть в 1 состояние, а не во все.

Будет порядка V^2, (вообще V^2 - V) вершин и V^3 ребер(оценка очень сверху), тк каждую из 2 машинок можно подвинуть в худшем случае в любую вершину, те сделать 2V ребер (граф полный). 
Кажется, точнее - VE

Далее - BFS - сложность - кол-во вершин  + кол-во ребер в графе состояний

Чтобы не двигаться назад - ставим пометку - расстояние. У соседа меньше => не идем в него
</details>

___

**4. Кратчайший путь на 0-1 графе**
![bfs7](/img/bfs7.jpg)
**Реализация на списке вершин, находящихся на заданном расстоянии**:
Добавляем стартовую вершину, далее смотрит соседей. Когда все соседи рассмотрены, вычеркиваем текущую вершину, смотрим соседей у следующей в текущем списке.

Ключевая идея - можем добавлять вершину в тот же список, из следующего списка можно не удалять
Критерий того, что вершина обработана - номер списка, в котором он а находится, не совпадает с кратчайшим расстоянием до нее

Кажется, легче использовать очередь и смотреть массив `dist[]`.
Восстановление ответа - так же, как в обычном BFS. 

Можно реализовать на деке (по сути очередь на 2 стеках):
в первой половине дека находятся вершины на расст. k-1, во второй половине - на расст k.\
Берем вершину слева, смотрим каждого соседа: если он на расстоянии 0, добавляем его в начало дека, если на расстоянии 1 еще не помеченый: помечаем числами, равными кратчайшему расстоянию, кладем в конец дека.

Обработана раньше или нет? - берем из дека и смотрим. (Придется хранить массив visited, либо прямо в деке хранить кратчайшее расстояние, как мы это делали с помощью индекса массива вершин, находящихся на заданном расстоянии)

---

**5. Кратчайший путь на 0-k графе**
![bfs8](/img/bfs8.jpg)
**Пример:** вершины - перекрестки, ребра - дороги

**Алгоритм:** Почти то же самое, что и 0-1 граф. 
Критерий того, что мы достигли всего - все ячейки массива после последней обработанной пусты.

Можем иметь очень много пустых списков (В худшем случае надо (V - 1) K) => храним номера непустых списков с помощью кучи минимумов.

Если кладем сами вершины в кучу, получаем алгоритм Дейкстры.

</details>

*That's all what I wanted to tell you.*







   
   









