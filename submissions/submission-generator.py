import os
import random
import datetime
from distutils.dir_util import copy_tree

readme = 'readme.md'
template_folder = "sample_submission"


def gen_random_name(length=8, alphabet="qwertyuiopasdfghjklzxcvbnm"):
    return "".join([random.choice(alphabet) for _ in range(length)])


def edit_readme(name, info, date=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")):
    txt = open(readme).read()
    new_row = f'''\t<tr>
            <td style="text-align:center">
                {date}
            </td>
            <td style="text-align:center">
                <a href="{name}/">{name}</a>
            </td>
            <td style="text-align:center">
                {info}
            </td>
            <td style="text-align:center">
                -
            </td>
            <td style="text-align:center">
                -
            </td>
        </tr>
    </tbody>
</table>'''
    txt = txt.replace("</tbody>\n</table>", new_row)

    with open(readme, 'w') as f:
        f.write(txt)


if __name__ == "__main__":
    info = input(f"Input model details for {readme}: ").strip()

    new_name = gen_random_name()
    os.makedirs(new_name)

    copy_tree(template_folder, new_name)

    # for f in os.listdir(new_name):
    #     if f[0] == '.':
    #         os.remove(os.path.join(new_name, f))

    with open(os.path.join(new_name, 'info.txt'), 'w') as f:
        f.write(info)

    edit_readme(new_name, info)

    print("New submission folder is available at", new_name + '/')
