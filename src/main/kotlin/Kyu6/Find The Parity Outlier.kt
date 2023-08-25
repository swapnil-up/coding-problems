package Kyu6

fun find(integers: Array<Int>): Int {
//    integers.forEach { println(it) }
//    println()
    for(i in 0..integers.size-1){
        if (Math.abs((integers[i])%2)!=Math.abs((integers[(i+1)%integers.size])%2))
            if (Math.abs((integers[(i+2)%integers.size])%2)!=Math.abs((integers[(i+1)%integers.size])%2)) return((integers[(i+1)%integers.size]))
            else return(integers[i])
    }
    return 0
}

fun main() {
    val exampleTest1 = arrayOf(2,6,8,-10,3)
    val exampleTest2 = arrayOf(206847684,1056521,7,17,1901,21104421,7,1,35521,1,7781)
    val exampleTest3 = arrayOf(Integer.MAX_VALUE, 0, 1)
    println(find(exampleTest1))
    println(find(exampleTest2))
    println(find(exampleTest3))
    println(find(arrayOf(160, 3, 1719, 19, 11, 13, -21)))
    println(find(arrayOf(2, 4, 0, 100, 4, 11, 2602, 36)))

}