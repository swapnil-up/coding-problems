package Kyu7

fun getMiddle(word : String) : String {
    if((word.count()+1)%2==0) return(word[(word.count()/2)].toString())
    else return(word.substring((word.count()/2)-1,((word.count()/2)+1)))
}
fun main() {
    println(getMiddle("test"));
    println(getMiddle("middle"));
    println(getMiddle("testing"));
    println(getMiddle("A"));
}