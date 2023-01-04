let second_first = 0;
let second_second = 0;
let mill_second = 0;
let mill_first = 0;
let intervalClock = null;
let data = [];
let str = [];
//스타트 버튼 클릭 시 실행 함수
document.querySelector(".start").addEventListener("click", () => {
  if (intervalClock == null) {
    intervalClock = setInterval(startClock, 10);
  }
});

// 스탑 버튼 클릭 시 실행 함수
document.querySelector(".stop").addEventListener("click", () => {
  stopClock();
  printRecord();
});

//리셋 버튼 클릭 시 실행 함수
document.querySelector(".reset").addEventListener("click", () => {
  resetClock();
});

//전체 선택 클릭 시 실행 함수
document
  .querySelector(".nav-select-all input")
  .addEventListener("click", (e) => {
    selectAll(e.target.checked);
  });

//삭제 버튼 클릭 시 실행 함수
document.querySelector(".nav-delete a").addEventListener("click", () => {
  items = document.querySelectorAll(".item-wrapper");
  deleteItem(items);
});

//스톱 워치 시작 함수
function startClock() {
  mill_second++;
  if (mill_second >= 10) {
    mill_second = 0;
    mill_first++;
  }
  if (mill_first >= 10) {
    second_second++;
    mill_second = 0;
    mill_first = 0;
  }
  if (second_second >= 10) {
    second_first++;
    second_second = 0;
  }
  printClock();
}

//시간 멈추는 함수
function stopClock() {
  if (intervalClock != null) {
    clearInterval(intervalClock);
    intervalClock = null;

    let temp = new Object();
    temp.second_first = second_first;
    temp.second_second = second_second;
    temp.mill_first = mill_first;
    temp.mill_second = mill_second;
    data.push(temp);
  }
}

//스톱워치 초기화 함수
function resetClock() {
  second_first = 0;
  second_second = 0;
  mill_second = 0;
  mill_first = 0;
  printClock();
}

//시간 출력 함수
function printClock() {
  document.querySelector(".second-first").textContent = second_first;
  document.querySelector(".second-second").textContent = second_second;
  document.querySelector(".millSecond-frist").textContent = mill_first;
  document.querySelector(".millSecond-second").textContent = mill_second;
}

function selectAll(ch) {
  document.querySelectorAll(".check").forEach((item) => {
    item.checked = ch;
  });
}

function deleteItem(items) {
  for (let i = 0; i < data.length; i++) {
    let str = "".concat(
      data[i].second_first,
      data[i].second_second,
      ":",
      data[i].mill_first,
      data[i].mill_second
    );
    for (let j = 0; j < items.length; j++) {
      if (items[j].childNodes[1].checked == true) {
        if (items[j].childNodes[3].textContent == str) {
          data.splice(i, 1);
          i--;
          items[j].remove();
          break;
        }
      }
    }
  }
  printRecord();
  document.querySelector(".nav-select-all input").checked = false;
}

function printRecord() {
  str = "";
  data.forEach((item) => {
    str += `<li>
                <div class = "item-wrapper">   
                        <input type="checkbox" class="check" />
                        <p>${item.second_first}${item.second_second}:${item.mill_first}${item.mill_second}</p>
                </div>
                </li>`;
  });

  document.querySelector(".record-list").innerHTML = str;
}
