
import Data.List (sort)
import System.IO (hIsEOF, stdin)

countSecondList :: [Int] -> Int -> Int -> Int -> Int
countSecondList lst1 n i val
    | i == n = 0
    | lst1 !! i /= val = 0
    | otherwise = 1 + countSecondList lst1 n (i+1) val

twoPointersSumProductCount :: [Int] -> [Int] -> Int -> Int -> Int -> Int
twoPointersSumProductCount lst1 lst2 n i j
    | i == n || j == n = 0
    | lst1 !! i < lst2 !! j = twoPointersSumProductCount lst1 lst2 n (i + 1) j
    | lst1 !! i > lst2 !! j = twoPointersSumProductCount lst1 lst2 n i (j + 1)
    | otherwise = let cntj = countSecondList lst2 n j (lst1 !! i)
                      cnti = countSecondList lst1 n i (lst1 !! i)
                  in (lst1 !! i) * cnti * cntj + twoPointersSumProductCount lst1 lst2 n (i + cnti) (j + cntj)

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

    let n = length sortedList1
    let result = twoPointersSumProductCount sortedList1 sortedList2 n 0 0

    print result