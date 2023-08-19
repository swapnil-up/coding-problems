package Kyu8

fun twiceAsOld(dadYearsOld: Int, sonYearsOld: Int): Int {
    var twice=sonYearsOld*2
    if(dadYearsOld>twice){
        return(dadYearsOld-twice)
    }
    else{
        return (twice-dadYearsOld)
    }
}


fun main(){
    println(twiceAsOld(36,7))
    println(twiceAsOld(55,30))
//        assertEquals(0, twiceAsOld(42,21))
//        assertEquals(20, twiceAsOld(22,1))
//        assertEquals(29, twiceAsOld(29,0))

}
