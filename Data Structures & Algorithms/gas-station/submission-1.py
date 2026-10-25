class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        starting_station = 0
        current_gas_surplus = 0
        total_gas_surplus = 0

        for station in range(len(gas)):

            gas_difference = gas[station] - cost[station]

            current_gas_surplus += gas_difference 
            total_gas_surplus += gas_difference 

            if current_gas_surplus < 0:
                starting_station = station +  1
                current_gas_surplus = 0

        return starting_station if total_gas_surplus >= 0 else -1