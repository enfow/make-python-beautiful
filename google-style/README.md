# Google Python Style Guide

- [Google Python Style Guide](<https://google.github.io/styleguide/pyguide.html>)

## 1. Background

Python은 Google에서 사용되는 대표적인 동적 언어입니다. 본 Style Guide에서는 Python 프로그램에서 사용해야 하거나, 반대로 사용하지 않아야 하는 경우들을 나열하고 있습니다. 

## 2. Python Language Rules

### 2.1 Lint

본 [pylintrc](<https://google.github.io/styleguide/pylintrc>)를 사용하여 `pylint`를 실행하십시오.

#### 2.1.1. Definition

pylint는 Python 소스코드에서 버그와 스타일 오류를 찾아주는 도구입니다. C, C++과 같은 Python과 비교해 보다 정적인 언어들의 컴파일러들이 잡아내어 주는 문제들을 찾아주는 도구라고도 할 수 있습니다. 다만 동적 언어로서의 특성을 많이 가지고 있는 Python의 특성상 때때로 부정확하다는 점을 알고 사용할 필요가 있습니다.

##### 2.1.2. Pros

오타나 `using-vars-before-assignment`와 같이 놓치기 쉬운 문제들을 잡아줍니다.

##### 2.1.3. Cons

pylint는 완벽하지 않습니다. 따라서 때때로 warning을 제거하거나, 수정해야 하기도 합니다.

##### 2.1.4. Decision

warning이 동작하지 않도록 할 때에는 아래와 같이 line-level comment를 사용할 수 있습니다.

```python
dict = 'something awful'  # Bad Idea... pylint: disable=redefined-builtin
```

pylint의 warning들은 empty-docstring 과 같은 심볼릭 네임으로 표현됩니다. Google의 warning들은 `g-` 로 시작합니다.

만약 warning을 제거하는 이유가 심볼릭 네임만으로 알기 어려운 경우에는 설명을 추가해주어야 합니다.

위와 같이 warning을 제거하게 되면 제거한 부분을 다시 찾아보기 쉽다는 장점이 있습니다.

pylint의 warning들은 다음 명령어를 통해 모두 출력할 수 있습니다([출력 결과](<./pylint_example/pylint_list_msgs.txt>)).

```bash
$ pylint --list-msgs
```

특정 warning에 대해서 알고 싶다면 아래와 같은 명령어를 사용하면 됩니다.

```bash
pylint --help-msg=C6409
```

warning을 제거할 때에는 `pylint: disable-msg`보다는 `pylint: disabale`을 사용합니다.

사용하지 않는 argument가 있으면 pylint에서 잡아냅니다(`unused_argument`). 하지만 아래 예시와 같이 함수의 시작과 함께 변수를 제거하도록 하여 warning을 없앨 수 있습니다. 이 경우 반드시 comment를 달아주어야 합니다.

```python
def viking_cafe_order(spam, beans, eggs=None):
    del beans, eggs  # Unused by vikings.
    return spam + spam + spam
```

사용하지 않는 변수에 대한 warning을 제거하는 또다른 방법은 `_` 또는 `unused_`를 변수명의 접두사로 사용하는 것입니다. 다만 이렇게 사용하는 것은 함수 내에서 해당 변수를 사용하지 않도록 강제하지는 않는다는 점에서 좋은 방법은 아닙니다. 이와 관련한 예시는 [본 링크](<./pylint_example/unused_argument.py>)에 정리해 두었습니다.
