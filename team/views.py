from django.shortcuts import render
from collections import namedtuple

# Create your views here.
from .models import Teams
from .models import Tournament
import random


def groupView(request):
    all_groups = {}  # this list will contain all 8 groups
    group_names = ["A", "B", "C", "D", "E", "F", "G", "H"]

    qualified_teams = Teams.objects.filter(last_year_qualifiers=True)
    non_qualified_teams = Teams.objects.filter(last_year_qualifiers=False)
    total_teams = len(qualified_teams) + len(non_qualified_teams)

    # forming a group of 4 team
    for i in range(8):
        group_4 = {}
        random.shuffle(list(qualified_teams))
        q_team = random.choice(qualified_teams)  # selected qualified team
        qualified_teams = qualified_teams.exclude(id=q_team.id)
        group_4[q_team.state] = q_team.name
        group_len = len(group_4)
        run_count = 0
        while group_len != 4 and run_count <= total_teams:
            # select a team and check its state and if its diff
            # then append it to the group
            random.shuffle(list(non_qualified_teams))
            another_team = random.choice(non_qualified_teams)
            if not another_team.state in group_4:
                non_qualified_teams = non_qualified_teams.exclude(id=another_team.id)
                group_4[another_team.state] = another_team.name
                group_len += 1

            run_count += 1
        all_groups[group_names[i]] = group_4
    this_year_teams = Tournament(data=all_groups)
    this_year_teams.save()

    context = {
        "qu_teams": qualified_teams,
        "nq_teams": non_qualified_teams,
        "group_4": group_4,
        "all_groups": all_groups,
    }
    return render(request, "team/index.html", context)
