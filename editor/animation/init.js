requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {
        var io = new extIO({
            multipleArguments: true,
            functions: {
                js: 'mostNumbers',
                python: 'checkio'
            }
        });
        io.start();
    }
);