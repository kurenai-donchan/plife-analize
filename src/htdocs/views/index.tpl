<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>P-life analize</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">

</head>

<body>

<nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
    <a class="navbar-brand" href="#">P-life analize</a>
</nav>

<main role="main" class="container">
    <input class="form-control" id="myInput" type="text" placeholder="Search..">
    <br>
    <div class="table-responsive">
    <table id="plife-data" class="table table-bordered table-striped">
        <colgroup class="">
        <% for i in range(4001, int(4267)): %>
        <colgroup class="{{slots_payout_data[sorted(slots_payout_data.keys())[len(slots_payout_data.keys()) - 1]][str(i)]['lotName']}}">
            <% end %>
        <thead style="background-color: white;">
        <tr>
            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
            <% for i in range(4001, int(4267)): %>
            <th>{{i}}<div style="display: none">{{slots_payout_data[sorted(slots_payout_data.keys())[len(slots_payout_data.keys()) - 1]][str(i)]['lotName']}}</div></th>
            <% end %>
        </tr>

        </thead>
        <tbody id="myTable">
        <% for key, value in slots_payout_data.items():%>
            <tr>
                <td>{{ key }}</td>
                <% for i in range(4001, int(4267)): %>
                    <% if (int(value[str(i)]['Payout']) >= 3000):
                        color = 'red'
                    elif(int(value[str(i)]['Payout']) <= -3000):
                        color = 'blue'
                    else:
                        color = ''
                    end %>
                    <td style="color: {{color}} ">
                        {{ value[str(i)]['Payout'] }}
                        <div style="display: none">
                            <p>{{ value[str(i)]['lotName'] }}</p>
                        </div>
                    </td>

                <% end %>
            </tr>
        <% end %>
        </tbody>
    </table>
    </div>
</main>


<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
<script src="/static/js/lib/jquery.floatThead.min.js"></script>

<script>
    $(document).ready(function(){
        $("#myInput").on("keyup", function() {
            var value = $(this).val().toLowerCase();
            $("#plife-data colgroup").filter(function() {
                var lotName = $(this).attr('class').toLowerCase();
                if(lotName.indexOf(value) > -1){
                    $(this).css('background-color', '#ffffe0');
                } else {
                    $(this).css('background-color', '');
                }
            });
        });
    });

</script>
</body>
</html>
