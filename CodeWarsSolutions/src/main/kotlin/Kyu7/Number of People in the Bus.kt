package Kyu7

fun people(busStops: Array<Pair<Int, Int>>) : Int {
    var count=0
    for(i in 0..<busStops.count()){
        count+=busStops[i].first
        count-=busStops[i].second
    }
    return(count)
}
fun main(){
    println(people(arrayOf(3 to 0,9 to 1,4 to 10,12 to 2,6 to 1,7 to 10)))
    println(people(arrayOf(3 to 0,9 to 1,4 to 8,12 to 2,6 to 1,7 to 8)))
    println(people(arrayOf(10 to 0,3 to 5,5 to 8)))
}