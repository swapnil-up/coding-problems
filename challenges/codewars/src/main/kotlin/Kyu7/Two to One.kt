package Kyu7

fun longest(s1:String, s2:String):String {
    return ((s1+s2).toCharArray().distinct().toSortedSet().joinToString(""))
}

fun main() {
    println("longest Fixed Tests")
    println(longest("aretheyhere", "yestheyarehere"))
    println(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
    println(longest("inmanylanguages", "theresapairoffunctions"))

}