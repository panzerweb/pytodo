from colorama import Fore, Style, init
init(autoreset=True)

# Search by yyyy-mm-dd
def search_by_date(target_date: str, arr: list) -> None:
    result = [task for task in arr if task["created_at"] == target_date]

    if result:
        print(Fore.CYAN + Style.BRIGHT + "\n═══════════════ SEARCH RESULTS ═══════════════\n")
        for i, task in enumerate(result, start=1):
            print(Fore.YELLOW + f"📝 Task {i}")
            print(Fore.WHITE + f"   • Task ID     : {task['id']}")
            print(f"   • Title : {task['todo']}")
            print(f"   • Description : {task['description']}")
            print(f"   • Created At  : {task['created_at']}")
            print(Fore.CYAN + "──────────────────────────────────────────────")
        print(Fore.GREEN + Style.BRIGHT + f"\n✅ {len(result)} task(s) found for {target_date}\n")
    else:
        print(Fore.RED + Style.BRIGHT + "⚠️  No tasks found or invalid date format.")
        print(Fore.LIGHTBLACK_EX + "   Try using format: yyyy-mm-dd\n")
