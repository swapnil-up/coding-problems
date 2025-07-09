package Kyu8

object Solution {
    fun areaOrPerimeter(l:Int, w:Int):Int {
        if (l==w) return(l*l) else return(2*(l+w))
    }
}

fun main() {
    println(Solution.areaOrPerimeter(2, 2))

    }