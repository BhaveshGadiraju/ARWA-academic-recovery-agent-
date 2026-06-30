from itertools import combinations


class CandidatePlanGenerator:
    """
    Generates intelligent recovery plans instead of
    blindly exploring every possible task combination.
    """

    def generate(
        self,
        tasks,
        available_time,
    ):

        # ----------------------------
        # Step 1
        # Score each task
        # ----------------------------

        ranked_tasks = sorted(

            tasks,

            key=self._task_priority,

            reverse=True,

        )

        candidate_plans = []

        # ----------------------------
        # Step 2
        # Generate plans of increasing size
        # ----------------------------

        max_tasks = min(
            len(ranked_tasks),
            6,
        )

        for size in range(1, max_tasks + 1):

            for combo in combinations(
                ranked_tasks,
                size,
            ):

                total_time = sum(

                    task.estimated_time

                    for task in combo

                )

                if total_time > available_time:
                    continue

                if not self._passes_constraints(combo):
                    continue

                candidate_plans.append(
                    list(combo)
                )

        # ----------------------------
        # Step 3
        # Remove duplicates
        # ----------------------------

        unique = []

        seen = set()

        for plan in candidate_plans:

            key = tuple(

                sorted(
                    task.id
                    for task in plan
                )

            )

            if key in seen:
                continue

            seen.add(key)

            unique.append(plan)

        return unique

    # -------------------------------------------------

    def _task_priority(
        self,
        task,
    ):

        score = 0

        score += task.points_value * 3

        score += max(
            0,
            72 - task.due_in_hours,
        )

        score -= task.difficulty * 2

        score -= task.estimated_time

        return score

    # -------------------------------------------------

    def _passes_constraints(
        self,
        tasks,
    ):

        high_difficulty = sum(

            task.difficulty >= 8

            for task in tasks

        )

        if high_difficulty > 2:
            return False

        urgent = any(

            task.due_in_hours <= 24

            for task in tasks

        )

        if not urgent:

            return False

        return True