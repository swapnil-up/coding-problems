package Kyu8

import kotlin.math.abs

fun elevator(left: Int, right: Int, call: Int): String {
    var leftDistance=abs(left-call)
    var rightDistance=abs(right-call)
    if (leftDistance>=rightDistance){
        return("right")
    }
    else{
        return("left")
    }
}

fun main(){
        var e1= elevator(0,1,0)
        println(e1)
//        assertEquals("right", elevator(0,1,1))
//        assertEquals("right", elevator(0,1,2))
//        assertEquals("right", elevator(0,0,0))
//        assertEquals("right", elevator(0,2,1))
    }