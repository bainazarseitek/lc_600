class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        places = {i: [] for i in range(n)}

        for frm, to, price in flights:
            places[frm].append((price, to))

        # (total_price, current_city, flights_left)
        minHeap = [(0, src, k + 1)]

        # Cheapest price found for:
        # (city, flights_left)
        best = {
            (src, k + 1): 0
        }

        while minHeap:
            total_price, city, flights_left = heapq.heappop(minHeap)

            # We already found a cheaper way to reach this exact state
            if total_price > best[(city, flights_left)]:
                continue

            if city == dst:
                return total_price

            if flights_left > 0:
                for price, to in places[city]:
                    new_price = total_price + price
                    new_state = (to, flights_left - 1)

                    if (
                        new_state not in best
                        or new_price < best[new_state]
                    ):
                        best[new_state] = new_price

                        heapq.heappush(
                            minHeap,
                            (
                                new_price,
                                to,
                                flights_left - 1
                            )
                        )

        return -1
