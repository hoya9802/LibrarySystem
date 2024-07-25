# LibrarySystemV.1.0 [Personal Project]

## Library of Implementation
 - tkinter, pandas, csv, datetime

### Version of Python
 - conda create -n "env name" python==3.8

## Dataset
 - [ID.csv](https://github.com/hoya9802/LibrarySystem/blob/main/data/ID.csv) : ID / PW / NAME / GEN / AGE / AUTH(ADMIN: 관리자계정, GUEST: 일반계정)
 - [book.csv](https://github.com/hoya9802/LibrarySystem/blob/main/data/book.csv) : BOOK_ISBN	/ BOOK_TITLE	/ BOOK_AUTHOR	/ BOOK_PUB / BOOK_PRICE /	STATUS(available(대출가능), unavailable(대출불가))
 - [check_in_out.csv](https://github.com/hoya9802/LibrarySystem/blob/main/data/check_in_out.csv) : ID /	BOOK /	EXPIRATION(대출 당일부터 14일까지)

## The Overall Structure
<p align="center">
<img width="770" alt="스크린샷 2024-07-25 오후 12 59 13" src="https://github.com/user-attachments/assets/99262b4d-9275-48eb-96fc-1d9681fc6d85">
</p>

## File Structure
### add.py
  - 도서 대출 파일입니다.
  - ISBN, NAME, AUTHOR, PUBLISHER, PRICE, STATUS를 차례대로 입력 받습니다.
  - 만약 빈칸이 존재하는 상태로 책을 추가하거나 기존에 있는 책을 추가하면 오류화면 출력합니다.
  - 존재하지 않는 책을 삭제하면 오류화면이 출력됩니다.
  - 추가된 도서는 Category 1.도서 목록에서 확인이 가능합니다.
  - 해당 코드는 [add.py](https://github.com/hoya9802/LibrarySystem/blob/main/add.py) 에서 확인이 가능합니다.

### bookList.py
  - book.csv에 들어있는 도서들을 확인할 수 있습니다.
  - 검색기능을 통해 자신이 원하는 책이 도서관에 있는지 확인 가능합니다.
  - 추가되거나 대출가능 여부를 실시간으로 확인이 가능합니다.
  - 해당 코드는 [bookList.py](https://github.com/hoya9802/LibrarySystem/blob/main/bookList.py) 에서 확인이 가능합니다.


### category.py
  - 메인 페이지로서 다양한 기능에 접근할 수 있습니다.
  - 일반계정은 2. 도서추가, 4. 회원관리 페이지에 접근이 불가능합니다.
  - 관리자계정은 모든 페이지에 접근이 가능합니다.
  - 해당 코드는 [category.py](https://github.com/hoya9802/LibrarySystem/blob/main/category.py) 에서 확인이 가능합니다.

### checkInOut.py
  - check_in_out.csv에서 로그인한 사용자의 대출상태를 확인 할 수 있습니다. (다른 사람의 대출내역은 확인 불가)
  - 자신이 대출하지 않은 책을 반납하려고 시도하면 오류화면이 출력됩니다.
  - book.csv에 존재하지 않는 책을 대출하려고 시도하거나 책의 상태가 대출불가인 책을 대출하려고 하면 오류화면이 출력됩니다.
  - 책을 반납하면 해당 책의 상태는 즉시 대출가능 상태로 변경되며, 마찬가지로 책을 대출하면 해당 책의 상태는 즉시 대출 불가상태로 변경됩니다.
  - 해당 코드는 [checkInOut.py](https://github.com/hoya9802/LibrarySystem/blob/main/checkInOut.py) 에서 확인이 가능합니다.

### function.py
  - 공통적으로 많이 쓰이는 함수들을 모아서 저장해 놓은 파일입니다.
  - csv_to_list() : csv파일을 불러와서 type을 list로 변경해주는 코드입니다.
  - display_csv_data() : 원하는 database를 화면에 출력해주는 코드입니다.
  - search() : entry에 들어온 값을 db와 비교하여 해당 값이 존재하면 화면에 출력해주는 코드입니다.
  - change_value() : db에서 원하는 row의 특정 column의 값을 변경하고 싶을 때 사용됩니다.
  - 해당 코드는 [function.py](https://github.com/hoya9802/LibrarySystem/blob/main/function.py) 에서 확인이 가능합니다.

### login.py
  - 로그인을 할 수 있는 페이지입니다.
  - 없는 계정으로 로그인을 시도하면 오류화면이 출력됩니다.
  - 계정별 다른 접근 권한을 가지고 있습니다.
  - 해당 코드는 [login.py](https://github.com/hoya9802/LibrarySystem/blob/main/login.py) 에서 확인이 가능합니다.
 
### main.py
  - 전체 코드를 실행할 수 있게 도와주는 파일입니다.
  - 해당 코드는 [main.py](https://github.com/hoya9802/LibrarySystem/blob/main/main.py) 에서 확인이 가능합니다.

### userList.py
  - 유저들에 계정 정보를 확인할 수 있는 페이지입니다. (일반계정 접근불가)
  - 원하는 계정을 검색하면 해당 계정이 존재하는 경우 화면에 출력됩니다.
  - 해당 코드는 해당 코드는 [userList.py](https://github.com/hoya9802/LibrarySystem/blob/main/userList.py) 에서 확인이 가능합니다.

## Key Development Points
 - 기능 하나하나가 많은 양의 코드를 필요로 하기 때문에 여러 .py파일로 분리하였습니다.
 - class와 function 기능을 서로 적절히 선택하여 코드의 간결성과 가독성을 증가시켰습니다.
 - GUI를 사용하여 사용자가 보다 쉽게 프로그램을 사용할 수 있도록 하였습니다.
 - 계정을 분리하여 일반 사용자가 민감한 정보에 접근을 할 수 없도록 설계하였습니다.
 - .csv 파일을 db로 사용하여 프로그램이 종료되어도 변경사항이 저장되도록 설계하였습니다.

## Issues
 - 아직까지는 발견되 이슈사항은 없습니다.
 - 향후 발견되면 업데이트 예정입니다.

## Future Updates
 - 회원가입 페이지를 추가할 예정입니다.
 - 해당책을 어느 나이대의 어느 성별이 대출하는지 추척하는 기능을 추가할 예정입니다.
 - 계정 삭제및 아이디/패스워드 변경 기능을 추가할 예정입니다.


