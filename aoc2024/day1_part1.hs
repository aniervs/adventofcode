import Data.List (sort)
import System.IO (hIsEOF, stdin)

computeManhattanDistance :: [Int] -> [Int] -> Int
computeManhattanDistance list1 list2 = sum $ zipWith (\x y -> abs (x - y)) list1 list2

readBothListsElementbyElement :: IO ([Int], [Int])
readBothListsElementbyElement = do

    eof <- hIsEOF stdin
    if eof
        then return ([], [])
        else do
            input <- getLine
            let numbers = words input 
            let num1 = read (numbers !! 0) :: Int
            let num2 = read (numbers !! 1) :: Int
            
            (list1, list2) <- readBothListsElementbyElement
            return (num1 : list1, num2 : list2)
    

main :: IO ()
main = do
    (list1, list2) <- readBothListsElementbyElement

    let sortedList1 = sort list1
    let sortedList2 = sort list2 
    
    let distance = computeManhattanDistance sortedList1 sortedList2
    print distance
    