# one liner to create folders and files within

Date: 2026-02-22 11:35

---

for i in {01..20}; do mkdir -p problem_$i && touch problem_$i/{main.py,test_main.py}; done

loop, make the directory then create the files
